from pydantic import BaseModel

class ResponseMessage(BaseModel): #this class is for validating and displaying data in http://127.0.0.1:8000/docs#/

    message: str #the response message that gets returned in the delete endpoints MUST look like: return "message": "whatver after"