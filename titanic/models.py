
from config import db, ma

# Passenger Class/Model
class Passenger(db.Model):
    __tablename__ = 'passengers'
    id = db.Column(db.Integer, primary_key=True)
    survived = db.Column(db.Boolean)
    passengerclass = db.Column(db.Integer)
    name = db.Column(db.String(255))
    sex = db.Column(db.String(10))
    age = db.Column(db.FLOAT)
    parentsorchildrenaboard = db.Column(db.Integer)
    siblingsorspousesaboard = db.Column(db.Integer)
    fare = db.Column(db.FLOAT)

    def __init__(self,survived,passengerclass,name,sex,age,siblingsorspousesaboard,parentsorchildrenaboard,fare):
        self.survived = survived
        self.passengerclass = passengerclass
        self.name = name
        self.sex = sex
        self.age = age
        self.siblingsorspousesaboard = siblingsorspousesaboard
        self.parentsorchildrenaboard = parentsorchildrenaboard
        self.fare = fare


# Passenger Schema
class PassengerSchema(ma.Schema ):
  passengerclass = ma.String(data_key="passengerClass")
  parentsorchildrenaboard = ma.String(data_key="parentsOrChildrenAboard")
  siblingsorspousesaboard = ma.String(data_key="siblingsOrSpousesAboard")
  class Meta:
    fields = ('id', 'survived', 'passengerclass','name','sex','age','siblingsorspousesaboard','parentsorchildrenaboard','fare')
