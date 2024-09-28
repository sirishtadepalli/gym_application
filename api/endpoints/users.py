from app.db.session import SessionLocal
from fastapi import APIRouter, HTTPException
from app import models, schemas
from typing import List
from pydantic import EmailStr

router = APIRouter()

@router.post("/users/", response_model=schemas.User)#this is a route for the /users endpoint.

def create_user(username: str, email: EmailStr, mobile_number: int, weight: int, height: int, body_fat_percentage: int ):#defines this function. parameter takes username, which should be a str

    user = models.User(name = username, email = email, mobile_number = mobile_number, weight = weight, height = height, body_fat_percentage = body_fat_percentage, active = True)#creates instance of User class defined above. Name attribute is set to argument

#the active and administrator are just set by default for now

    db = SessionLocal()

    db.add(user) #add's user object to the session

    db.commit()#means that any changes made in the session will be saved to database

    db.refresh(user)#refreshes the session in case adding user causes an auto response values in db

    db.close()#you need to close the session after use. This flushes

    return user 


@router.get("/users/{user_id}", response_model= schemas.User)#retrives user by user_id

def read_user(user_id : int):#this function takes an int for the parameter

    db = SessionLocal()
    
    user = db.query(models.User).filter(models.User.id == user_id).first()#queries User table, where id column == function argument

    print(vars(user)) #delete this later

    db.close()#standard in every function

    if not user:

        db.close()

        raise HTTPException(status_code=404, detail="User not found")#throws exception if that user doesn't exist
    
    return user


@router.get("/users/", response_model= List[schemas.User]) #retrieves a list of users

def read_users(skip: int = 0, limit: int = 10):#2 parameters, which are limits and set to default values

    db = SessionLocal()

    users = db.query(models.User).offset(skip).limit(limit).all()#this retrieves first 10 users, skipping every other one

    db.close()

    return users


@router.put("/users/{user_id}", response_model=schemas.User)#put is for updating an existing resource

def update_user(user_id: int, name: str = None, email: EmailStr = None, mobile_number : int = None, weight: int = None, height : int = None, body_fat_percentage : int = None, active : bool = None):

    db = SessionLocal()
    
    user = db.query(models.User).filter(models.User.id == user_id).first()#searches User table for id == user_id in argument

    if not user: #if you don't find it then do all this

        db.close()

        raise HTTPException(status_code=404, detail="User not found")

    if name is not None:
        user.name = name#sets the name column of that row to name in argument

#TODO the email
    if email is not None:
        user.email = email

    if mobile_number is not None:
        user.mobile_number = mobile_number

    if weight is not None:
        user.weight = weight

    if height is not None:
        user.height = height

    if body_fat_percentage is not None:
        user.body_fat_percentage = body_fat_percentage

    if active is not None:
        user.active = active

    db.commit()#anytime you make changes

    db.refresh(user)#same

    db.close()#same

    return user


@router.delete("/users/{user_id}", response_model= schemas.ResponseMessage)#deletes user by user_id

def delete_user(user_id: int):#takes int user_id as parameter

    db = SessionLocal()

    user = db.query(models.User).filter(models.User.id == user_id).first()#searches table for that user

    if not user:

        db.close()

        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)#deletes that row

    db.commit()#standard

    db.close()#standard

#TODO code has executed until this line but the message below is what caused an error
    return {"message": f"User id {user_id} was deleted."}

