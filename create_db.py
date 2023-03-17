from web_app import app,db
from models.model import User
import hashlib

def init_db():
    with app.app_context():
        db.reflect()
        db.drop_all()
        db.create_all()

#creates userid and password to login
def createseed():
    data={
        'username': "Admin",
        'password': hashlib.sha256("test@123".encode('utf-8')).hexdigest()
    }
    users = User(**data)
    db.session.add(users)
    db.session.commit()


init_db()
createseed()