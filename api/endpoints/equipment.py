#remember all this stuff that you are importing. You must use all of them below or don't import it. 
from app.db.session import SessionLocal
from fastapi import APIRouter, HTTPException 
from app import models, schemas 
from typing import List

router = APIRouter() 

'''Always start with @router. and then the type of route command it will be. In the following paranthesis, the /route
name/ in double quotes, and then response_model = the class in the schemas that this is for. 
Now def the function that this route will call.'''

@router.post("/equipment/", response_model=schemas.Equipment)#this is a route for the /equipment endpoint.

def add_equipment(name: str, brand: str, cost: float):

    '''Now you are making an object from the models class using the arguments entered to = the class attributes
    and a SessionLocal object which helps add everything to the database.'''

    equipment = models.Equipment(name = name, brand = brand, cost = cost)

    db = SessionLocal()

    db.add(equipment) #adds the equipment object to the database

    db.commit()

    db.refresh(equipment)

    db.close() #necessary step every time. 

    return equipment

@router.get("/equipment/{name}", response_model= schemas.Equipment)

def find_equipment(name: str): #enter an id number for argument

    db = SessionLocal()

    equipment = db.query(models.Equipment).filter(models.Equipment.name == name).first()

    db.close()

    if not equipment:

        db.close()

        raise HTTPException(status_code=404, detail="Equipment not found")

    return equipment

@router.get("/equipment/", response_model= List[schemas.Equipment])

def list_equipment():

    db = SessionLocal()

    list = db.query(models.Equipment).all()

    db.close() #standard

    return list

@router.put("/equipment/{id}", response_model= schemas.Equipment)

def update_equipment(id: int, name: str = None, brand: str = None, cost: float = None):

    '''You set the default values of these arguments as none because you don't have to fill them out if you
    don't want to update them. But you need the id because that's how it finds that exercise.'''

    db = SessionLocal()

    '''first create an object based on existing database row by searching for it.'''
    equipment = db.query(models.Equipment).filter(models.Equipment.id == id).first() #if it's only one then you need to specify first()

    '''if no equipment match was found...'''
    if not equipment:

        db.close()

        raise HTTPException(status_code=404, detail="Equipment not found")
    
    '''The default values for these arguments were set to none, which means you don't have to enter them in.
    But if you did, because you want to update them, then it will set the object attributes to equal those arguments.'''

    if name is not None:

        equipment.name = name

    if brand is not None:

        equipment.brand = brand

    if cost is not None:

        equipment.cost = cost


    db.commit()

    db.refresh(equipment)

    db.close()

    '''And this is always the last step.'''
    return equipment

@router.delete("/equipment/{name}", response_model= schemas.ResponseMessage) #this is the only one that has a different response model

def delete_equipment(name: str):

    db = SessionLocal()

    equipment = db.query(models.Equipment).filter(models.Equipment.name == name).first()

    if not equipment:

        db.close()

        raise HTTPException(status_code=404, detail="Equipment not found")

    db.delete(equipment)

    db.commit()

    db.close()

    return {"message" : f"{name} has been deleted."}
