from pydantic import BaseModel, Field
from datetime import datetime

class TokenEntry(BaseModel):
    token: str = Field(..., min_length=1)
    expires_at: datetime