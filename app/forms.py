from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.fields.choices import SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired(), Length(min=2, max=120)])
    login = StringField('Login', validators=[DataRequired(), Length(min=2, max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('Avatar', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Register')

    def validate_login(self, field):
        user = User.query.filter_by(login=field.data).first()
        if user:
            raise ValidationError('Please enter a valid login.')


class LoginForm(FlaskForm):
    login = StringField('Username', validators=[DataRequired(), Length(min=2, max=120)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class StudentForm(FlaskForm):
    student = SelectField('student', choices=[], render_kw={'class': 'form-control'})


class TeacherForm(FlaskForm):
    teacher = SelectField('teacher', choices=[], render_kw={'class': 'form-control'})
