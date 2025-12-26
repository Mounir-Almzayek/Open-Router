"""
Provider Routing Configuration
"""
from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from app.enums import ProviderSort, DataCollection, Quantization


class MaxPrice(BaseModel):
    """Maximum price configuration"""
    prompt: Optional[str] = None
    completion: Optional[str] = None
    request: Optional[str] = None
    image: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        if self.prompt is not None:
            result["prompt"] = self.prompt
        if self.completion is not None:
            result["completion"] = self.completion
        if self.request is not None:
            result["request"] = self.request
        if self.image is not None:
            result["image"] = self.image
        return result


class ProviderConfig(BaseModel):
    """Provider routing configuration"""
    order: Optional[List[str]] = None
    allow_fallbacks: bool = True
    require_parameters: bool = False
    data_collection: Optional[DataCollection] = None
    zdr: Optional[bool] = None
    enforce_distillable_text: Optional[bool] = None
    only: Optional[List[str]] = None
    ignore: Optional[List[str]] = None
    quantizations: Optional[List[Quantization]] = None
    sort: Optional[ProviderSort] = None
    max_price: Optional[MaxPrice] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        if self.order is not None:
            result["order"] = self.order
        if self.allow_fallbacks is not None:
            result["allow_fallbacks"] = self.allow_fallbacks
        if self.require_parameters is not None:
            result["require_parameters"] = self.require_parameters
        if self.data_collection is not None:
            result["data_collection"] = self.data_collection.value
        if self.zdr is not None:
            result["zdr"] = self.zdr
        if self.enforce_distillable_text is not None:
            result["enforce_distillable_text"] = self.enforce_distillable_text
        if self.only is not None:
            result["only"] = self.only
        if self.ignore is not None:
            result["ignore"] = self.ignore
        if self.quantizations is not None:
            result["quantizations"] = [q.value for q in self.quantizations]
        if self.sort is not None:
            result["sort"] = self.sort.value
        if self.max_price is not None:
            result["max_price"] = self.max_price.to_dict()
        return result

