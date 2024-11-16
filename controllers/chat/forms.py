from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ChatForm(FlaskForm):
    user_input = StringField('Enter your message', validators=[DataRequired()])
    submit = SubmitField('Send')