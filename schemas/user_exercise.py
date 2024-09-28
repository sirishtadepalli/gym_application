from pydantic import BaseModel
from typing import Optional, List


class UserExercise(BaseModel): #this class is for validating and displaying data in http://127.0.0.1:8000/docs#/

    user_id: int
    
    exercise_id: int

    exercise_day: str

    