"""
Annotation Processor
"""
from typing import List, Dict, Any
from app.models.responses import ChatResponse
from app.processors.base_processor import BaseResponseProcessor


class AnnotationProcessor(BaseResponseProcessor):
    """Process annotations (citations, file annotations)"""
    
    def extract_annotations(self, response: ChatResponse) -> List:
        """Extract all annotations"""
        annotations = []
        if response.choices:
            message = response.choices[0].message
            if message.annotations:
                annotations = message.annotations
        return annotations
    
    def extract_url_citations(self, response: ChatResponse) -> List[Dict[str, Any]]:
        """Extract URL citations"""
        citations = []
        annotations = self.extract_annotations(response)
        
        for annotation in annotations:
            if annotation.type == "url_citation":
                citations.append({
                    "url": annotation.url_citation.url,
                    "title": annotation.url_citation.title,
                    "content": annotation.url_citation.content,
                    "start_index": annotation.url_citation.start_index,
                    "end_index": annotation.url_citation.end_index
                })
        
        return citations
    
    def process(self, response: ChatResponse) -> Dict[str, Any]:
        """Process response and extract annotations"""
        return {
            "annotations": self.extract_annotations(response),
            "citations": self.extract_url_citations(response)
        }

