from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "beetlejuice"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

app.app_context().push()
# ACCESS FLASK WITHIN IPYTHON AND HAVE SESSIONS

@app.route('/')
def show_home_page():
    """Displays a home page with all pets."""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add_pet', methods = ['POST', 'GET'])
def add_a_pet_form_and_process():
    """ Renders a pet form for 'GET' and 
    processes the 'POST' by validating the information and adding it to the database -> redirects to home OR 
    if invalid form information, then the form loads again with error messages. """
    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name = name, species = species, photo_url = photo_url, age=age, notes= notes, available=available)
        db.session.add(pet)
        db.session.commit()
        flash(f"Created new pet: {name} ")
        return redirect('/')
    
    return render_template('petform.html', form = form)

@app.route('/<int:pet_id>/edit', methods = ['POST', 'GET'])
def edit_pet(pet_id):
    """ Renders the same form AND page as the add_a_pet_form_process. 
    Uses the current pet.id to prefill the form. 
    processes the 'POST' by validating the information and adding it to the database -> redirects to home OR 
    if invalid form information, then the form loads again with error messages. 
    """
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj = pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()
        flash(f"Updated pet: {pet.name} ")
        return render_template('pet_page.html', pet=pet)
    
    return render_template('petform.html', form = form)

@app.route('/<int:pet_id>')
def view_pet_page(pet_id):
    """ Renders a page to show all pet instance data from the database. """
    pet = Pet.query.get_or_404(pet_id)
    
    return render_template('pet_page.html', pet=pet)

