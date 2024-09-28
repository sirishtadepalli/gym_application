from fastapi import APIRouter
from app.api.endpoints import exercise
from app.api.endpoints import users
from app.api.endpoints import user_exercise #these are the variables that the functions in endpoints returns
from app.api.endpoints import equipment
from app.api.endpoints import payment

'''This page is the one that actually creates the display in the url that you make in the schemas'''
api_router = APIRouter()#this will be imported in the main file

api_router.include_router(users.router, prefix="/gym", tags=["users"]) #tags creates a header for that db table's actions
api_router.include_router(exercise.router, prefix="/gym", tags=["exercise"])
api_router.include_router(user_exercise.router, prefix="/gym", tags=["user_exercises"])
api_router.include_router(equipment.router, prefix="/gym", tags=["equipment"])
api_router.include_router(payment.router, prefix= "/gym", tags=["payment"])

''''this imports the entire contents of the users.py file but all you want is the variable router, which you then use
in the include_router function. The prefix and tags is for the display in the api'''