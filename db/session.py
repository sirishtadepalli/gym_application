from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

database_url = "sqlite:///./test.db"#this is the database's url saved as a variable

engine = create_engine(database_url)#you have to use the create_engine function and feed it the url

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)#sessions are your time for interacting with the db

