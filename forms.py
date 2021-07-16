"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField , FloatField, SelectField , BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, Required


class AddPetForm(FlaskForm):
    """Form for adding pets, accepts name, species, photo_url, age, notes, available"""

    name = StringField( "Pet Name", validators=[InputRequired()])
    species = StringField( "Species", validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField( 'Age Group',
                        choices = [ ('Baby' , 'Baby' )  ,  ('Young', 'Young'  ), ( 'Adult', 'Adult') , ('Senior' , 'Senior' )     ],
                        coerce = str, validators=[InputRequired()]
                        )
    notes = StringField( 'Notes', validators=[Optional()] )
    available = BooleanField( 'Availability')

class EditPetForm(FlaskForm):
    """Form for editing pet photo_url, notes and availability"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    
    notes = StringField( 'Notes', validators=[Optional()] )

    available = BooleanField( 'Availability')

