from app import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100))
