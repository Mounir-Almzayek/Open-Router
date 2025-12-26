"""
Stream Processor
"""
from typing import AsyncIterator, List, Optional
from app.models.responses import StreamChunk, ChatResponse, MessageResponse
from app.enums import FinishReason


class StreamProcessor:
    """Process streaming responses"""
    
    @staticmethod
    async def collect_stream(
        stream: AsyncIterator[StreamChunk]
    ) -> ChatResponse:
        """Collect streaming chunks into complete response"""
        collected_content = ""
        collected_reasoning = []
        tool_calls = []
        finish_reason = None
        model = None
        id = None
        
        async for chunk in stream:
            if chunk.id:
                id = chunk.id
            if chunk.model:
                model = chunk.model
            
            for choice in chunk.choices:
                if choice.delta.content:
                    collected_content += choice.delta.content
                if choice.delta.reasoning_details:
                    collected_reasoning.extend(choice.delta.reasoning_details)
                if choice.delta.tool_calls:
                    tool_calls.extend(choice.delta.tool_calls)
                if choice.finish_reason:
                    finish_reason = choice.finish_reason
        
        # Build complete response
        message = MessageResponse(
            role="assistant",
            content=collected_content,
            reasoning_details=collected_reasoning if collected_reasoning else None,
            tool_calls=tool_calls if tool_calls else None
        )
        
        from app.models.responses import ChoiceResponse, ChatResponse
        choice = ChoiceResponse(
            index=0,
            message=message,
            finish_reason=finish_reason
        )
        
        return ChatResponse(
            id=id,
            model=model,
            choices=[choice]
        )
    
    @staticmethod
    async def process_stream_chunk(chunk: StreamChunk) -> dict:
        """Process single stream chunk"""
        result = {
            "id": chunk.id,
            "model": chunk.model,
            "content": "",
            "reasoning": [],
            "tool_calls": []
        }
        
        for choice in chunk.choices:
            if choice.delta.content:
                result["content"] += choice.delta.content
            if choice.delta.reasoning_details:
                result["reasoning"].extend(choice.delta.reasoning_details)
            if choice.delta.tool_calls:
                result["tool_calls"].extend(choice.delta.tool_calls)
            if choice.finish_reason:
                result["finish_reason"] = choice.finish_reason.value
        
        return result

