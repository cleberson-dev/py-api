from pydantic import BaseModel

class CreatePostRequest(BaseModel):
  title: str
  content: str

class PostResponse(BaseModel):
  id: int
  title: str
  content: str