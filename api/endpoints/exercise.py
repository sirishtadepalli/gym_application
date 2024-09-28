from app.db.session import SessionLocal
from fastapi import APIRouter, HTTPException
from app import models, schemas
from typing import List
from pydantic import EmailStr

router = APIRouter()


@router.post("/exercise/", response_model=schemas.Exercise)  # this is a route for the /exercises endpoint.
def create_exercise(exercise_name: str, exercise_category: str, exercise_recommended_weight: int, exercise_recommended_sets: int, exercise_recommended_reps: int, exercise_recommended_interval: int = 0):
                 # defines this function. parameter takes exercisename, which should be a str

    exercise = models.Exercise(exercise_name=exercise_name, exercise_category=exercise_category, exercise_recommended_weight=exercise_recommended_weight, exercise_recommended_sets=exercise_recommended_sets, exercise_recommended_reps=exercise_recommended_reps,
                       exercise_recommended_interval=exercise_recommended_interval)# creates instance of exercise class defined above. Name attribute is set to argumenn# the active and administrator are just set by default for now

    db = SessionLocal()

    db.add(exercise)  # adds exercise object to the session

    db.commit()  # means that any changes made in the session will be saved to database

    db.refresh(exercise)  # refreshes the session in case adding exercise causes an auto response values in db

    db.close()  # you need to close the session after use. This flushes

    return exercise


@router.get("/exercise/{exercise_name}", response_model=schemas.Exercise)  # retrives exercise by exercise_name
def read_exercise(exercise_name: str):  # this function takes an int for the parameter

    db = SessionLocal()

    exercise = db.query(models.Exercise).filter(
        models.Exercise.exercise_name == exercise_name).first()  # queries exercise table, where exercise_name column == function argument

    db.close()  # standard in every function

    if not exercise:
        db.close()

        raise HTTPException(status_code=404, detail="Exercise not found")  # throws exception if that exercise doesn't exist

    return exercise


@router.get("/exercise/", response_model=List[schemas.Exercise])  # retrieves a list of exercises
def read_exercise(skip: int = 0, limit: int = 10):  # 2 parameters, which are limits and set to default values

    db = SessionLocal()

    exercise = db.query(models.Exercise).offset(skip).limit(
        limit).all()  # this retrieves first 10 exercises, skipping none

    db.close()

    return exercise


@router.put("/exercise/{exercise_id}", response_model=schemas.Exercise)  # put is for updating an existing resource
def update_exercise(exercise_id: int, exercise_name: str = None, exercise_category: str = None,
                    exercise_recommended_weight: int = None,
                    exercise_recommended_sets: int = None, exercise_recommended_reps: int = None,
                    exercise_recommended_interval: int = 0):

    db = SessionLocal()

    exercise = db.query(models.Exercise).filter(
        models.Exercise.exercise_id == exercise_id).first()  # searches exercise table for id == exercise_id in argument

    if not exercise:  # if you don't find it then do all this

        db.close()

        raise HTTPException(status_code=404, detail="exercise not found")

    if exercise_name is not None:
        exercise.exercise_name = exercise_name  # sets the name column of that row to name in argument

    if exercise_category is not None:
        exercise.exercise_category = exercise_category

    if exercise_recommended_weight is not None:
        exercise.exercise_recommended_weight = exercise_recommended_weight

    if exercise_recommended_sets is not None:
        exercise.exercise_recommended_sets = exercise_recommended_sets

    if exercise_recommended_reps is not None:
        exercise.exercise_recommended_reps = exercise_recommended_reps

    if exercise_recommended_interval is not None:
        exercise.exercise_recommended_interval = exercise_recommended_interval

    db.commit()  # anytime you make changes

    db.refresh(exercise)  # same

    db.close()  # same

    return exercise


@router.delete("/exercise/{exercise_id}", response_model=schemas.ResponseMessage)  # deletes exercise by exercise_id
def delete_exercise(exercise_id: int):  # takes int exercise_id as parameter

    db = SessionLocal()

    exercise = db.query(models.Exercise).filter(models.Exercise.exercise_id == exercise_id).first()  # searches table for that exercise

    if not exercise:
        db.close()

        raise HTTPException(status_code=404, detail="exercise not found")

    db.delete(exercise)  # deletes that row

    db.commit()  # standard

    db.close()  # standard

    # TODO code has executed until this line but the message below is what caused an error
    return {"message": f"exercise id {exercise_id} was deleted."}

