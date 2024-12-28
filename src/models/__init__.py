from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user.user_model import User
from .people.people_model import People
from .planet.planet_model import Planet
from .favorite.favorite_model import Favorite