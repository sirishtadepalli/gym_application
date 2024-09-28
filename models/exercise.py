from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from db.base import Base
from sqlalchemy.orm import relationship
from typing import List
from models.user_exercises import UserExercises
from db.session import engine



class Exercise(Base):  # this class is for defining the actual database table

    __tablename__ = "exercise"  # remember, class name is not necessarily the table name. Here you specify the table name.

    exercise_id = Column(Integer, primary_key=True, index=True,
                autoincrement=True)  # So this is one field/column in the table. it is a primary key

    exercise_name = Column(String, index=True)  # here is another column in the table.

    exercise_category = Column(String)

    exercise_recommended_weight = Column(Integer)

    exercise_recommended_sets = Column(Integer)

    exercise_recommended_reps = Column(Integer)

    exercise_recommended_interval = Column(Integer)
