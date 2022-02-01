from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class AddItemForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()], render_kw={'placeholder': 'Título', 'autocomplete': 'off'})
    description = TextAreaField('Descrição', validators=[DataRequired()], render_kw={'placeholder': 'Descrição', 'autocomplete': 'off'})
    submit = SubmitField('Adicionar', render_kw={'class': 'button'})    