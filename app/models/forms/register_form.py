from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length



class RegisterForm(FlaskForm):
    name = StringField('Name', render_kw={'placeholder': 'Name'}, validators=[DataRequired(), Length(min=4, max=100, message='Name must contain between 4 and 100 characters')])
    username = StringField('Username', render_kw={'placeholder': 'Username'}, validators=[DataRequired(), Length(min=4, max=30, message='Username must contain between 4 and 30 characters!')])
    email = EmailField('Email', render_kw={'placeholder': 'Email'}, validators=[DataRequired(), Email(message='Invalid Email!')])
    password = PasswordField('Password', render_kw={'placeholder': 'Password'}, validators=[DataRequired(), Length(min=8, message="The password must be at least 8 characters!")])
    confirm_password = PasswordField('Confirm password', render_kw={'placeholder': 'Confirm password'}, validators=[DataRequired()])
    submit = SubmitField('Register', render_kw={'class': 'button'})