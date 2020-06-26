from fastapi import FastAPI
from routes import posts_router
from database import Base, engine
import models



Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
def hello():
  return { "Olá": "Mundinho" }

app.include_router(posts_router, prefix="/posts")