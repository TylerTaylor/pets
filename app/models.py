#1. ✅ Build out Pet Model

# Import from sqlalchemy: PrimaryKeyConstraint, Column, String, Integer

# Import from sqlalchemy.ext.declarative, declarative_base  

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    breed = db.Column(db.String)
    temperament = db.Column(db.String)

    owners_of_pet = db.relationship('PersonPet', backref = 'pet')

class Person(db.Model):

    __tablename__ = "people"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

    pets_of_owner = db.relationship('PersonPet', backref = 'person')

class PersonPet(db.Model):

    __tablename__ = "people_pets"

    id = db.Column(db.Integer, primary_key = True)

    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('people.id'))

#1.a ✅ Initialize declarative_base and assign it to a variable called Base

#1.b ✅ Create a class Pet that inherits from Base

    # Set the "__tablename__" to 'pets
    # Add table args for a primary key constraint based off the id

    #Create the following columns
        # id -> type integer
        # name -> type string
        # species -> type string
        # breed -> type string
        # temperament -> type string
        # owner_id -> type integer 

    # Add a __repr__ method that returns a string containing the id, name, species, breed and temperament of our class
    
#Note: Nothing further goes in this file.

# In the the following section, we will generate a number of folders and files

#2. ✅ Migrations 
# In the app directory, run `alembic init migrations`
# Your directory structure should look like the following:
# └── migrations
#     └── versions
#     ├── env.py
#     ├── README
#     ├── script.py.mako
# ├── alembic.ini
# ├── console.py
# └── models.py

#2.b Configuration
    # In alembic.ini, find `sqlalchemy.url` and set it to `sqlalchemy.url = sqlite:///pet_app.db`
    # In env.py, find `target_metadata` and add `from models import Base` above it. 
    # Next, set target_metadata to `target_metadata = Base.metadata`

#2.c ✅ Generate a migration by running `alembic revision --autogenerate -m "Added Pet model"`
    
    # pet_app.db should have been added to your file structure

    # Take the time to review the migration and verify the database with SQLite Explorer or DB Browser

# 3. ✅ Head to debug.py to test out CRUD actions