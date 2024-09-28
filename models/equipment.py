from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DECIMAL
from sqlalchemy.orm import relationship
from typing import List
from db.base import Base
from models.exercise import Exercise
from models.user_exercises import UserExercises

class Equipment(Base):

    __tablename__ = 'equipment'

    id = Column(Integer, primary_key = True, index = True, autoincrement = True) #the autoincrement is so that when you create a new row in the endpoints, you just have to enter the name and stuff, and it'll automatically create an id number for it which is the very next number.

    name = Column(String)

    brand = Column(String)

    cost = Column(DECIMAL)