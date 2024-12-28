from flask import Blueprint, jsonify, request
from models import User, db

user_bp = Blueprint("user_bp", __name__ )

@user_bp.route("/user/create", methods=["POST"])
def create_user():  
    user_data = request.get_json()
    if "is_active" in user_data:
        user_data["is_active"] = user_data["is_active"] == True
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()
    return "usuario creado", 201

@user_bp.route("/user/get", methods=["GET"])
def get_list_user():
   list_user = User.query.all()
   list_user = [user.serialize() for user in list_user]  
   return jsonify({"list_user":list_user})

@user_bp.route("/user/get/<int:id>", methods=["GET"])
def get_user(id):
   user = User.query(id)
     
   return jsonify({"user":user.serialize()})