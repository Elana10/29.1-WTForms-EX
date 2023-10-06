from models import Pet, db
from app import app

#Create all tables -- based on the python Class model.py 
db.drop_all()
db.create_all()

p1 = Pet(name = "Happy", species = "dog", age = 5, photo_url = 'https://boostlikes-bc85.kxcdn.com/blog/wp-content/uploads/2018/04/Short-URL-Illustration.jpg', notes = "Kid friendly")

p2 = Pet(name = "Fluffy", species = "cat")

p3 = Pet(name = "Spike", species = "porcupine")

db.session.add_all([p1,p2,p3])
db.session.commit()