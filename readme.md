from dbs import db
from sqlalchemy.orm import relationship

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10),nullable=False,unique=True)

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    python = db.Column(db.Integer,default=0)
    big_data = db.Column(db.Integer,default=0)
    h5 = db.Column(db.Integer,default=0)
    total_score = db.Column(db.Integer,default=0)
    key_1 = db.Column(db.Integer,db.ForeignKey("student.id"))
    g_cus = relationship('Student', backref='rfind')