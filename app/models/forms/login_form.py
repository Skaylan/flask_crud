from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()], render_kw={'placeholder': 'Username'})
    password = PasswordField('Senha', validators=[DataRequired()], render_kw={'placeholder': 'Password'})
    submit = SubmitField('Entrar', render_kw={'class': 'button'})