from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class AddItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={'placeholder': 'Title', 'autocomplete': 'off'})
    description = TextAreaField('Description', validators=[DataRequired()], render_kw={'placeholder': 'Description', 'autocomplete': 'off'})
    submit = SubmitField('Add', render_kw={'class': 'button'})    