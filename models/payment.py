from sqlalchemy import Column, Integer, String
from db.base import Base

class Payment(Base):

    __tablename__ = "payment"

    order = Column(Integer, primary_key = True, index = True, autoincrement = True)

    user_id = Column(Integer)

    street = Column(String)

    city = Column(String)

    state = Column(String)

    zip = Column(Integer)

    card = Column(Integer)

    exp_month = Column(Integer)

    exp_year = Column(Integer)

    cvv = Column(Integer)

    purchase_day = Column(Integer)

    purchase_month = Column(Integer)

    purchase_year = Column(Integer)

    product = Column(String)
