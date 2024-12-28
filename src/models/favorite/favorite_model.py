
from sqlalchemy import Enum

from .. import db

from enum import Enum as PyEnum  # Importar la clase Enum de Python

# Definir la enumeración correctamente
class MyEnum(str, PyEnum):
    PEOPLE = "people"
    PLANET = "planet"
    
  

class Favorite(db.Model):
    favorite_id = db.Column(db.Integer, primary_key=True)  
    typeFavorite = db.Column(db.Enum(MyEnum, name="myenum"), nullable=False)
 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  
    user = db.relationship('User', back_populates='favorites')

    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    planet = db.relationship('Planet', back_populates='favorites')

    
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    people = db.relationship('People', back_populates='favorites')

    def serialize(self):
            return {}