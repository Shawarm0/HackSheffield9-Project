from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import DataRequired


class DysgraphiaForm(FlaskForm):
    audio = FileField(validators=[DataRequired()])
    submit = SubmitField()
    text = StringField(validators=[DataRequired()])


class AudioUploadForm(FlaskForm):
    audio_file = FileField(
        "Upload Audio File",
        validators=[FileRequired(), FileAllowed(["m4a"], "M4A files only!")],
    )
    submit = SubmitField("Upload")
