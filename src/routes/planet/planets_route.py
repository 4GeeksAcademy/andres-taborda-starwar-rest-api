from flask import Blueprint,jsonify, request
from models import Planet, db

planets_bp = Blueprint('planets_bp',__name__)

@planets_bp.route("/", methods=["GET"])
def get_planets():
    list_planets = Planet.query.all()
    list_planets = [planets.serialize() for planets in list_planets]  
    return jsonify({"list_planets":list_planets})

@planets_bp.route("/<int:planets_id>", methods = ["GET"]) 
def get_planet(planets_id):
        planet = Planet.query(planets_id)
        return jsonify({"planet":planet.serialize()})

@planets_bp.route('/create',methods=['POST'])
def create_user():
    user_data = request.get_json()
    new_planet = Planet(**user_data)
    db.session.add(new_planet)
    db.session.commit()
    return jsonify({"msg":"Planet created succesfull"}),201