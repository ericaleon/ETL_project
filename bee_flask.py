# import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, jsonify

# Database Setup
#################################################
# create engine
engine = create_engine("mysql://root:ericaDB@localhost/honeybees")
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the bee data and pesticide use tables
bees = Base.classes.bees_data
pests = Base.classes.pesticides

# Create our session (link) from Python to the DB
session = Session(engine)


# Flask Setup
#################################################
app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome, honeybees! <br/>"
        f"Available Routes:<br/>"
        f"/api/honey-yield<br/>"
        f"/api/greatest-change"
    )


@app.route("/api/honey-yield")
def honey():
    """Returns a list of states' honey yield per colony"""
    # Query all states' bee colony & honey production data in descending order
    sel = "bees.state, bees.end_colonies,bees.colony_yield, bees.production"
    results = session.query(*sel).\
        order_by(bees.colony_yield.desc()).\
        all()

    # Convert list of tuples into normal list
    all_prod = list(np.ravel(results))

    return jsonify(all_prod)


@app.route("/api/greatest-change")
def change():
    """Return a list of colony change data including the state, colony change, and pesticide use"""
    # Query bees and pesticides tables
    results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)