from flask import Blueprint, jsonify, request
from models import Favorite, User, People, Planet, db


favorites_bp= Blueprint('favorites_bp', __name__)

@favorites_bp.route('/people/<int:people_id>', methods=['POST'])
def add_favorite_person(people_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    person = People.query.get(people_id)
    if not user or not person:
      return jsonify({'error': 'User or Person not found'}), 404
    favorites = Favorite(user_id=user.id, people_id=person.id)
    db.session.add(favorites)
    db.session.commit()
    return jsonify({'message': 'Person added to favorites'})

@favorites_bp.route('/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    planet = Planet.query.get(planet_id)
    if not user or not planet:
      return jsonify({'error': 'User or Planet not found'}), 404
    favorites = Favorite(user_id=user.id, planet_id=planet.id)
    db.session.add(favorites)
    db.session.commit()
    return jsonify({'message': 'Planet added to favorites'})

@favorites_bp.route('/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_person(people_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    person = People.query.get(people_id)
    if not user or not person:
      return jsonify({'error': 'User or Person not found'}), 404
    favorites = Favorite(user_id=user.id, people_id=person.id)
    db.session.delete(favorites)
    db.session.commit()
    return jsonify({'message': 'Person deleted from favorites'})

@favorites_bp.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    user_id = request.args.get('user_id')
    user = User.query.get(user_id)
    planet = Planet.query.get(planet_id)
    if not user or not planet:
      return jsonify({'error': 'User or Planet not found'}), 404
    favorites = Favorite(user_id=user.id, planet_id=planet.id)
    db.session.delete(favorites)
    db.session.commit()
    return jsonify({'message': 'Planet deleted from favorites'})