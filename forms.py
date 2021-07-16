"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField , FloatField, SelectField , BooleanField


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField( "Pet Name")
    species = StringField( "Specie")
    photo_url = StringField("Photo URL")
    age = SelectField( 'Age Group',
                        choices = [ ('Baby' , 'Baby' )  ,  ('Young', 'Young'  ), ( 'Adult', 'Adult') , ('Senior' , 'Senior' )     ],
                        coerce = str
                        )
    notes = StringField( 'Notes' )
    available = BooleanField( 'Availability')


