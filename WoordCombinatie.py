from app import db
from sqlalchemy import Column , String

class WoordCombinatie(db.Model):
    nederlands =  db.Column(db.String(255),primary_key=True)
    frans = db.Column(db.String(255))