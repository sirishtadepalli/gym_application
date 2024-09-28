from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from db.base import Base
from sqlalchemy.orm import relationship


class UserExercises(Base): #this class is for defining the actual database table

    __tablename__ = "UserExercises" #remember, class name is not necessarily the table name. Here you specify the table name.
    
    user_id = Column(Integer, ForeignKey("User.id"), primary_key = True, index = True) #So this is one field/column in the table.
    
    exercise_id = Column(Integer, ForeignKey("Exercise.exercise_id"), primary_key = True, index = True) #here is another column in the table.

    exercise_day = Column(String)

    