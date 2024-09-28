from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from typing import List
from db.base import Base
from models.exercise import Exercise
from models.user_exercises import UserExercises


class User(Base): #this class is for defining the actual database table

    __tablename__ = "users" #remember, class name is not necessarily the table name. Here you specify the table name.
    
    id = Column(Integer, primary_key = True, index = True, autoincrement = True) #So this is one field/column in the table. it is a primary key
    
    name = Column(String, index = True) #here is another column in the table.

    email = Column(String, index = True) #this column is an EmailStr which expects an @.com

    mobile_number = Column(Integer, index = True)

    weight = Column(Integer)

    height = Column(Integer)

    body_fat_percentage = Column(Integer)

    active = Column(Boolean) #will be true or false


# New Endpoint to this API
# API: Model (Table, Columns, Types)  -> Schema (Validations of inputs/output) -> Endpoint (GET, POST, PUT, DELETE) -> API (Router)
# Database : Create table -> Insert some test data


