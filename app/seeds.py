from app import app # required if using Flask-SQLAlchemy
from models import db, Pet, Person, PersonPet

from faker import Faker

fake = Faker() # faker data

if __name__ == '__main__':
    with app.app_context(): # required if using Flask-SQLAlchemy

        # SQLAlchemy seeding

        # clear out models
        Pet.query.delete()
        Person.query.delete()
        PersonPet.query.delete()

        # create models
        pets = [
            Pet (
                name = "Fido",
                species = "dog",
                breed = "golden retriever",
                temperament = "friendly"
            ),
            Pet (
                name = "Millie",
                species = "cat",
                breed = "maine coon",
                temperament = "charming"
            ),
            Pet (
                name = "Dave",
                species = "cow",
                breed = "Gurnsey",
                temperament = "happy"
            )
        ]

        # add objects to db
        db.session.add_all(pets)

        people = []

        for i in range(20):
            fake_person = Person (
                name = fake.name()
            )

            people.append(fake_person)

        db.session.add_all(people)

        people_pets = [
            PersonPet (
                person_id = 1,
                pet_id = 1
            ),
            PersonPet (
                person_id = 1,
                pet_id = 2
            ),
            PersonPet (
                person_id = 2,
                pet_id = 3
            )
        ]

        db.session.add_all(people_pets)

        # commit CREATE - UPDATE - DELETE actions
        db.session.commit()