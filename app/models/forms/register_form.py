from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length



class RegisterForm(FlaskForm):
    name = StringField('nome', render_kw={'placeholder': 'Name'}, validators=[DataRequired(), Length(min=4, max=100, message='Nome deve conter entre 4 e 100 caracteres!')])
    username = StringField('Usuario', render_kw={'placeholder': 'Username'}, validators=[DataRequired(), Length(min=4, max=30, message='Nome de usuario deve conter entre 4 e 30 caracteres')])
    email = EmailField('Email', render_kw={'placeholder': 'Email'}, validators=[DataRequired(), Email(message='Email Invalido!')])
    password = PasswordField('Senha', render_kw={'placeholder': 'Password'}, validators=[DataRequired(), Length(min=8, message="A senha deve no minimo 8 caracteres!")])
    confirm_password = PasswordField('Confirmar senha', render_kw={'placeholder': 'Confirm password'}, validators=[DataRequired()])
    submit = SubmitField('Register', render_kw={'class': 'button'})