from app import app # required if using Flask-SQLAlchemy

from models import db, Pet, Person, PersonPet

import time

if __name__ == '__main__':
    with app.app_context(): # required if using Flask-SQLAlchemy

        print("Welcome to my app!")

        pet_name = input("What is your pet's name? ") # requests user input
        pet_species = input("What is your pet's species? ")
        pet_breed = input("What is your pet's breed? ")
        pet_temp = input("What is your pet's temperament? ")

        your_pet = Pet (
            name = pet_name,
            species = pet_species,
            breed = pet_breed,
            temperament = pet_temp
        )

        db.session.add(your_pet)

        db.session.commit()

        one_pet = Pet.query.filter(Pet.name == pet_name).one()

        print("Figuring out your pet...")

        time.sleep(4) # pauses the CLI runtime for given number of seconds

        print("Got it!")

        print(one_pet.name + " is your pet! What a cute name!")