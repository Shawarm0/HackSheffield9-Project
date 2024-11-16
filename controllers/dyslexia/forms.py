from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DyslexiaForm(FlaskForm):
    big_text = StringField(validators=[DataRequired()])
    submit = SubmitField()
