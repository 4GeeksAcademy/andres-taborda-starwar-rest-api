from .. import db

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Integer)
    skin_color = db.Column(db.String(50))
    species = db.Column(db.String(50))

    homeworld_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    homeworld = db.relationship('Planet', back_populates='people')
    
    favorites = db.relationship('Favorite', back_populates='people')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name, 
            "height": self.height,
            "skin_color": self.skin_color,
            "species": self.species
        }