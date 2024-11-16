from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class DyslexiaForm(FlaskForm):
    big_text = TextAreaField("Text to Convert", validators=[DataRequired()])
    submit = SubmitField("Convert to Speech")
