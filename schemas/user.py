from pydantic import BaseModel, EmailStr#EmailStr is a special datatype for validating email addresses
from typing import Optional


class User(BaseModel): #this class is for validating and displaying data in http://127.0.0.1:8000/docs#/

    id: Optional[int] #why is this optional?

    name: str

    email: EmailStr

    mobile_number: int

    weight: int

    height: int

    body_fat_percentage: int

    active: bool = True#optional attribute that says if a user is active or not, True or False

