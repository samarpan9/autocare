from web_app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String


#class for users table
class User(db.Model):

    __tablename__ = "user_detail"
    __table_args__ = {'schema' : 'auth'}

    user_id             = Column(Integer, primary_key=True)
    user_name           = Column(String(100))
    passhash            = Column(String(100))
    phone_number        = Column(String(100))
    rec_status          = Column(String(100))
    rec_date            = Column(String(30), default = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

#class for bookings table
class Booking(db.Model):

    __tablename__ = "bookings"
    __table_args__ = {'schema' : 'sc_info'}

    book_id             = Column(Integer, primary_key=True)
    user_id             = Column(String(10))
    garage_id           = Column(String(10))
    service_ids         = Column(String(200))
    timing              = Column(String(100))
    delivery            = Column(String(10))
    user_loc            = Column(String(100))
    brand               = Column(String(50))
    brand_model         = Column(String(100))
    rec_date            = Column(String(30), default = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])


#class for Subscription table
class Subscription(db.Model):

    __tablename__ = "subscription_list"
    __table_args__ = {'schema' : 'sc_info'}

    sub_id              = Column(Integer, primary_key=True)
    user_id             = Column(String(10))
    garage_id           = Column(String(10))
    service_ids         = Column(String(200))
    package_id          = Column(String(10))
    rec_date            = Column(String(30), default = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])


    










