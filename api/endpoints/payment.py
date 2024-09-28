# remember all this stuff that you are importing. You must use all of them below or don't import it.
from app.db.session import SessionLocal
from fastapi import APIRouter, HTTPException, Query
from app import models, schemas
from typing import List

router = APIRouter()

'''Always start with @router. and then the type of route command it will be. In the following paranthesis, the /route
name/ in double quotes, and then response_model = the class in the schemas that this is for. 
Now def the function that this route will call.'''


@router.post("/payment/", response_model=schemas.Payment)  # this is a route for the /equipment endpoint.
def add_payment(user_id: int, street: str, city: str, state: str, zip: int, card: int, exp_month: int, exp_year: int,
                cvv: int, purchase_day: int, purchase_month: int, purchase_year: int, product: str):
    '''Now you are making an object from the models class using the arguments entered to = the class attributes
    and a SessionLocal object which helps add everything to the database.'''

    payment = models.Payment(user_id= user_id, street = street, city =city, state = state, zip = zip, card = card,
                             exp_month = exp_month, exp_year = exp_year, cvv = cvv, purchase_day = purchase_day,
                             purchase_month = purchase_month, purchase_year = purchase_year, product = product)


    db = SessionLocal()

    db.add(payment)  # adds the equipment object to the database

    db.commit()

    db.refresh(payment)

    db.close()  # necessary step every time.
    print(payment)
    return payment #if there is a validation error then error is here


'''3 ways to pass parameters to an endpoint, the path parameter, the query parameter, and the body parameter.
In the @router... that's the path parameter, in the function parameter below, that's the query parameter,'''
@router.get("/payment/", response_model=List[schemas.Payment])
def find_payment(id : int, id_type : str = Query(None, enum=["order", "user"])):  # enter an order number for argument

    db = SessionLocal()

    if id_type == 'order':
        single_payment = db.query(models.Payment).filter(models.Payment.order == id).first()

        payment = [single_payment]

    if id_type == 'user':

        payment = db.query(models.Payment).filter(models.Payment.user_id == id).all()

    db.close()

    if not payment:
        db.close()

        raise HTTPException(status_code=404, detail="Transaction not found")

    return payment


@router.get("/all_payments/", response_model=List[schemas.Payment])
def list_payments():
    db = SessionLocal()

    list = db.query(models.Payment).all()

    db.close()  # standard

    return list

'''body parameters are'''
@router.put("/payment/{order}", response_model=schemas.Payment)
def update_equipment(order: int, user_id: int = None, street: str = None, city: str = None, state: str = None, zip: int = None,
                     card : int = None, exp_month : int = None, exp_year: int = None, cvv : int = None, purchase_day: int = None,
                     purchase_month: int = None, purchase_year: int = None, product : str = None ):
    '''You set the default values of these arguments as none because you don't have to fill them out if you
    don't want to update them. But you need the id because that's how it finds that exercise.'''

    db = SessionLocal()

    '''first create an object based on existing database row by searching for it.'''
    payment = db.query(models.Payment).filter(
        models.Payment.order == order).first()  # if it's only one then you need to specify first()

    '''if no equipment match was found...'''
    if not payment:
        db.close()

        raise HTTPException(status_code=404, detail="Transaction not found")

    '''The default values for these arguments were set to none, which means you don't have to enter them in.
    But if you did, because you want to update them, then it will set the object attributes to equal those arguments.'''

    if user_id is not None:
        payment.user_id = user_id

    if street is not None:
        payment.street = street

    if city is not None:
        payment.city = city

    if state is not None:
        payment.state = state

    if zip is not None:
        payment.zip = zip

    if card is not None:
        payment.card = card

    if exp_month is not None:
        payment.exp_month = exp_month

    if exp_year is not None:
        payment.exp_year = exp_year

    if cvv is not None:
        payment.cvv = cvv

    if purchase_day is not None:
        payment.purchase_day = purchase_day

    if purchase_month is not None:
        payment.purchase_month = purchase_month

    if purchase_year is not None:
        payment.purchase_year = purchase_year

    if product is not None:
        payment.product = product

    db.commit()

    db.refresh(payment)

    db.close()

    '''And this is always the last step.'''
    return payment

@router.put("/payment2/{order}", response_model=schemas.Payment)
def update_body_parameters(order: int, payment : schemas.UpdatePayment):
    '''Made a new class in the Schemas.Payment file called Update Payment which contains all the attributes that I can just
    feed into this function here instead of typing them all out. You also made those attributes optional so that you wouldn't
    be '''

    print(payment.__dict__)
    db = SessionLocal()
    old_payment = db.query(models.Payment).filter(
        models.Payment.order == order).first()

    if not old_payment:
        db.close()

        raise HTTPException(status_code=404, detail="Transaction not found")

    print(payment.street)
    '''The whole JSON file that it generates in the API page is payment.__dict__. It's in dict format.'''

    for key, value in payment.__dict__.items():

        setattr(old_payment, key, value)



    db.commit()

    db.refresh(old_payment)

    db.close()

    
    return old_payment


@router.delete("/payment/{order}",
               response_model=schemas.ResponseMessage)  # this is the only one that has a different response model
def delete_payment(order: int):
    db = SessionLocal()

    payment = db.query(models.Payment).filter(models.Payment.order == order).first()

    if not payment:
        db.close()

        raise HTTPException(status_code=404, detail="Payment not found")

    db.delete(payment)

    db.commit()

    db.close()

    return {"message": f"order number {order} has been deleted."}
