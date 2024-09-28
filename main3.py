from fastapi import FastAPI, HTTPException
from app.api import api
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)#this part will usually be commented out unless you need to create a brand new table

app = FastAPI() #app is an instance, which will be used later.

app.include_router(api.api_router)# this takes the api_router from the api.py file

'''Find the list of exercise names based on user name. 
The output should print the user name, exercise names, and days.'''



'''uvicorn app.main3:app --reload
http://127.0.0.1:8000/docs#/ is for the API'''