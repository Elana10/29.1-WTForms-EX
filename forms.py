from flask_wtf import FlaskForm
from wtforms import StringField, URLField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional

class PetForm(FlaskForm):
    """Pet form for adding OR editing."""
    name = StringField("Pet Name", validators = [InputRequired(message = "Must include a pet name.")])
    species = SelectField("Species Type", 
                          choices = [['cat', 'Cat'], ['dog', 'Dog'], ['porcupine', 'Porcupine']],
                          validators = [InputRequired(message = "Must include a species type.")])
    photo_url = URLField("Image URL")
    age = FloatField("Enter Age", validators = [Optional()])
    notes = StringField("Notes About the Pet")
    available = BooleanField("Pet Available", 
                             default = True)
