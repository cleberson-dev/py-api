import os
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



DB = os.environ['POSTGRES_DB']
USER = os.environ['POSTGRES_USER']
PASSWORD = os.environ['POSTGRES_PASSWORD']
HOST = 'localhost'



url = f'postgresql://{USER}:{PASSWORD}@{HOST}/{DB}'
engine = sqlalchemy.create_engine(url)
session = sessionmaker(bind=engine)()
Base = declarative_base()