import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), unique=True, nullable=False)
    name = Column(String(250))
    last_name = Column(String(250))
    email = Column(Integer, unique=True, nullable=False)
    password = Column(String(250))


class Planet(Base):
    __tablename__= 'Planets'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    population = Column(String(250))
    Terrain = Column(String(250))
    climate = Column(String(50))

class Character(Base):
    __tablename__= 'Characters'
    id = Column(Integer, primary_key=True)
    gender = Column(String(50))
    description = Column(String(250))
    hair_color = Column(String(50))
    eyes_color = Column(String(50))
    height = Column(String(50))

class favoriteCharacter(Base):
    __tablename__= 'favotire_Characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    users = relationship(User)
    character_id = Column(Integer, ForeignKey('Characters.id'))
    characters = relationship(Character)

class favoritePlanet(Base):
    __tablename__ = 'favorite_Planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    users = relationship(User)
    planet_id = Column(Integer, ForeignKey('Characters.id'))
    planet = relationship(Character)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
