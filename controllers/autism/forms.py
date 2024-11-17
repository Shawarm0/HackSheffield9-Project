from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AutismForm(FlaskForm):
    user_input = StringField('Enter Text', validators=[DataRequired()])
    submit = SubmitField('Submit')