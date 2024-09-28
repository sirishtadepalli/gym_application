from pydantic import BaseModel

class Equipment(BaseModel): #schema class is always (BaseModel), model class is always (Base)

    #now all the columns but the datatypes are written in the short form
    id : int

    name: str

    brand: str

    cost: float