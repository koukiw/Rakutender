from pydantic import BaseModel

class Rakuten(BaseModel):
  text: str
  num: int
