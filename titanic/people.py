"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import Flask, request, jsonify
from config import db
from models import Passenger,PassengerSchema


def list():
    """
    This function responds to a request for /api/people/

    """
    
    all_passengers = Passenger.query.all()
    # Init schema
    passengers_schema = PassengerSchema(many=True)
    
    result = passengers_schema.dump(all_passengers)
    return jsonify(result)

def add(person):
    """
    This function updates an existing person in the people structure

    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    survived = request.json['survived']
    passengerClass = request.json['passengerClass']
    name = request.json['name']
    sex = request.json['sex']
    age = request.json['age']
    siblingsOrSpousesAboard = request.json['siblingsOrSpousesAboard']
    parentsOrChildrenAboard = request.json['parentsOrChildrenAboard']
    fare = request.json['fare']

    new_passenger = Passenger(survived, passengerClass, name, sex, age, siblingsOrSpousesAboard, parentsOrChildrenAboard, fare)

    db.session.add(new_passenger)
    db.session.commit()

    # Init schema
    passenger_schema = PassengerSchema()

    return passenger_schema.jsonify(new_passenger)

