from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class DysgraphiaForm(FlaskForm):
    audio = FileField(validators=[DataRequired()])
    submit = SubmitField()
  