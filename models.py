"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet """

    __tablename__ = "pets"

    id = db.Column( 
                    db.Integer,
                    Primary_Key=True, 
                    nullable = False, 
                    autoincrement = True
                    )

    name = db.Column(
                    db.Text,
                    nullable = False

                    )

    species = db.Column(
                    db.Text,
                    nullable = False
                        )

    photo_url = db.Columnn(
                    db.Text,
                    nullable = False,
                    default = ''
                        )

    age = db.Column(
                    db.Text, 
                    nullable = False,
                        # .in_([ 'Baby' , 'Young', 'Adult', 'Senior' ])

                     )

    notes = db.column(
                    db.Text
                    )
    
    available =  db.column(
                        db.Boolean ,
                        nullable = False,
                        default = True
                    )