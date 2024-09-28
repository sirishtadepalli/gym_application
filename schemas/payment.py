from pydantic import BaseModel
from typing import Optional

class Payment(BaseModel):

    order: int

    user_id: int

    street: str

    city: str

    state: str

    zip: int

    card: int

    exp_month: int

    exp_year: int

    cvv: int

    purchase_day: int

    purchase_month: int

    purchase_year: int

    product: str

class UpdatePayment(BaseModel):



    user_id: Optional [int] = None

    street: Optional [str] = None

    city: Optional [str] = None

    state: Optional [str]= None

    zip: Optional [int]= None

    card: Optional [int]= None

    exp_month: Optional [int]= None

    exp_year: Optional [int]= None

    cvv: Optional [int]= None

    purchase_day: Optional [int]= None

    purchase_month: Optional [int]= None

    purchase_year: Optional [int]= None

    product: Optional [str]= None
