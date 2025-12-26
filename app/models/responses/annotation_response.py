"""
Annotation Response Models
"""
from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel


class URLCitation(BaseModel):
    """URL citation"""
    url: str
    title: Optional[str] = None
    content: Optional[str] = None
    start_index: Optional[int] = None
    end_index: Optional[int] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"url": self.url}
        if self.title is not None:
            result["title"] = self.title
        if self.content is not None:
            result["content"] = self.content
        if self.start_index is not None:
            result["start_index"] = self.start_index
        if self.end_index is not None:
            result["end_index"] = self.end_index
        return result


class Annotation(BaseModel):
    """Annotation (citation)"""
    type: Literal["url_citation"]
    url_citation: URLCitation
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "type": self.type,
            "url_citation": self.url_citation.to_dict()
        }

