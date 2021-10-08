"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import Flask, request, jsonify
from config import db
from models import Passenger,PassengerSchema


def get(uuid):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people

    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Init schema
    passenger_schema = PassengerSchema()

    passenger = Passenger.query.get(uuid)
    return passenger_schema.jsonify(passenger)

def update(uuid,person):
    """
    This function updates an existing person in the people structure

    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    passenger = Passenger.query.get(uuid)
    
    survived = request.json['survived']
    passengerClass = request.json['passengerClass']
    name = request.json['name']
    sex = request.json['sex']
    age = request.json['age']
    siblingsOrSpousesAboard = request.json['siblingsOrSpousesAboard']
    parentsOrChildrenAboard = request.json['parentsOrChildrenAboard']
    fare = request.json['fare']

    passenger.survived = survived
    passenger.passengerClass = passengerClass
    passenger.name = name
    passenger.sex = sex
    passenger.age = age
    passenger.siblingsOrSpousesAboard = siblingsOrSpousesAboard
    passenger.parentsOrChildrenAboard = parentsOrChildrenAboard
    passenger.fare = fare

    db.session.commit()

    # Init schema
    passenger_schema = PassengerSchema()
    return passenger_schema.jsonify(passenger)



def delete(uuid):
    """
    This function deletes a person from the people structure

    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    passenger = Passenger.query.get(uuid)

    db.session.delete(passenger)
    db.session.commit()

    # Init schema
    passenger_schema = PassengerSchema()
    return passenger_schema.jsonify(passenger)
