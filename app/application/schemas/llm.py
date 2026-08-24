from typing import Literal

from pydantic import BaseModel, Field

#This is used for validating the LLM configuration 
class LLMConfig(BaseModel):
    provider: Literal["nvidia"]
    model_name: str = Field(min_length=1)
    temperature: float = Field(
        default=0.0,
        ge=0.0,
        le=2.0,
    )