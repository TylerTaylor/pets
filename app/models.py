from flask_sqlalchemy import SQLAlchemy

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