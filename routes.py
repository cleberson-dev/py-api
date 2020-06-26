from fastapi import APIRouter

from schemas import PostResponse, CreatePostRequest
from models import Post
from database import session



posts_router = APIRouter()

# Posts Router
@posts_router.get("/")
def get_posts():
  return session.query(Post).all()

@posts_router.post("/", response_model=PostResponse)
def create_post(create_post_request: CreatePostRequest):
  new_post = Post(
    title=create_post_request.title,
    content=create_post_request.content
  )

  session.add(new_post)
  session.commit()

  response = PostResponse(
    id=new_post.id,
    title=new_post.title,
    content=new_post.content,
  )

  return response