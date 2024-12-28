from .. import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    climate = db.Column(db.String(100))
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(100))
    
    people = db.relationship('People', back_populates='homeworld')
    favorites = db.relationship('Favorite', back_populates='planet')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "terrain": self.terrain
        }