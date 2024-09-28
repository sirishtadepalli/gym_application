from app.db.session import SessionLocal
from fastapi import APIRouter, HTTPException
from app import models, schemas
from typing import List
from pydantic import EmailStr

router = APIRouter()

@router.get("/UserExercises/{user_id}", response_model= List[schemas.UserExercise])#retrives exercise id and exercise days based on user id

def read_user_exercise(user_id : int):#this function takes an int for the parameter

    db = SessionLocal()
    
    user_exercise = db.query(models.UserExercise).filter(models.UserExercise.user_id == user_id).all() #queries User table, where id column == function argument
    
    print(user_exercise) #testing the variable remove later

    db.close()#standard in every function

    if not user_exercise:

        db.close()

        raise HTTPException(status_code=404, detail="Data for user not found")#throws exception if that user doesn't exist
    
    return user_exercise

'''Takes username and retrieves exercise names and day'''
@router.get("/UserExercises/{user_name}", response_model= List[schemas.UserExercise])#retrives exercise id and exercise days based on user id

def read_user_exercise(user_name : str):#this function takes an str for the parameter

    db = SessionLocal()
    
'''SELECT u.name, e.exercise_name, ue.exercise_day --output

FROM users u --the table where the input is

JOIN UserExercises ue --the other table that you are joining

ON u.id = ue.user_id --what connects the FROM table and the JOIN table?

JOIN exercise e --third table being joined

ON ue.exercise_id = e.exercise_id;

statement = select(Users, UserExercises).join(UserExercises) #
        results = session.exec(statement) #just always have this part
        for Users, UserExercises in results:
            print("User:", User, "Team:", team)'''

