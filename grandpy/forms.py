from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Length

class inputRequest(FlaskForm):
    question = StringField('Quelle est votre question ? ',
                            validators= [Length(min=2, max=30)])
