from pydantic import BaseModel
from typing import Optional, List


class Exercise(BaseModel): #this class is for validating and displaying data in http://127.0.0.1:8000/docs#/

    exercise_id: Optional[int]

    exercise_name: str

    exercise_category: str

    exercise_recommended_weight: int

    exercise_recommended_sets: int

    exercise_recommended_reps: int

    exercise_recommended_interval: int