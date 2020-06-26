from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine



class Post(Base):
  __tablename__ = 'post'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  content = Column(String)

  def __repr__(self):
    return f'Post({self.id})<{self.title}>'