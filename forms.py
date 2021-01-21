from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email, InputRequired, Regexp


class AttendanceForm(FlaskForm):
    saturday = BooleanField('Saturday')
    sunday = BooleanField('Sunday')
    wednesday = BooleanField('Wednesday')
    submit = SubmitField('Submit')