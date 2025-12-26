"""
Translation Service Endpoint
"""
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from typing import List
from app.services import OpenRouterClient
from app.dependencies import get_openrouter_api_key
from app.builders import ChatRequestBuilder
from app.exceptions import ValidationError, OpenRouterAPIError
from app.config import settings

router = APIRouter(prefix="/api/v1", tags=["translation"])


def get_client(api_key: str = Depends(get_openrouter_api_key)) -> OpenRouterClient:
    """Get OpenRouter client"""
    return OpenRouterClient(api_key=api_key)


class TranslationRequest(BaseModel):
    """Translation request model"""
    lang: List[str] = Field(..., description="List of language codes to translate to")
    word: str = Field(..., description="Text to translate")


class TranslationPair(BaseModel):
    """Translation pair"""
    key: str = Field(..., description="Language code")
    translation: str = Field(..., description="Translated text")


class TranslationResponse(BaseModel):
    """Translation response model"""
    translations: List[TranslationPair] = Field(..., description="List of translation pairs")


@router.post("/translate", response_model=TranslationResponse)
async def translate(
    request: TranslationRequest,
    client: OpenRouterClient = Depends(get_client)
):
    """
    Translate text to multiple languages
    
    Uses xiaomi/mimo-v2-flash:free model for translation.
    """
    try:
        # Build the prompt
        languages_str = ", ".join(request.lang)
        prompt = f"""Translate the following text to these languages: {languages_str}

Text to translate: {request.word}

Return the translations as a JSON object where each key is a language code and the value is the translation.
Return only valid JSON, no additional text.

Example format:
{{
  "ar": "الترجمة بالعربية",
  "en": "Translation in English",
  "fr": "Traduction en français"
}}"""

        # Create structured output schema
        schema = {
            "type": "object",
            "properties": {
                lang_code: {"type": "string"} for lang_code in request.lang
            },
            "required": request.lang,
            "additionalProperties": False
        }

        # Build the request using ChatRequestBuilder
        builder = ChatRequestBuilder()
        chat_request = (builder
            .with_model("xiaomi/mimo-v2-flash:free")
            .with_text(prompt)
            .with_structured_output(schema, name="TranslationResult", strict=True)
            .build())

        # Send request to OpenRouter
        response = await client.chat_completion(chat_request)
        
        # Extract the structured output
        if response.choices and response.choices[0].message.content:
            import json
            try:
                # Parse the JSON response
                content = response.choices[0].message.content
                if isinstance(content, str):
                    translations_dict = json.loads(content)
                else:
                    translations_dict = content
                
                # Convert to list of pairs
                translation_pairs = [
                    TranslationPair(key=lang_code, translation=translations_dict.get(lang_code, ""))
                    for lang_code in request.lang
                ]
                
                return TranslationResponse(translations=translation_pairs)
            except json.JSONDecodeError as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Failed to parse translation response: {str(e)}"
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="No response content received from translation model"
            )
    
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except OpenRouterAPIError as e:
        raise HTTPException(status_code=e.status_code or 500, detail=e.message)
    except Exception as e:
        import traceback
        error_detail = str(e)
        if settings.debug:
            error_detail += f"\n\nTraceback:\n{traceback.format_exc()}"
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=error_detail)

