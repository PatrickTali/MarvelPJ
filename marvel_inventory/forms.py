from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField
from wtforms. validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()]) 
    submit_button = SubmitField()


class CharacterForm(FlaskForm):
    name = StringField('name')
    description = StringField('description')
    comics_appeared_in = IntegerField('comics_appeared_in')
    super_power = StringField('super_power')
    date_created = DateField('date_created')
    dad_joke = StringField('dad joke')
    submit_button =SubmitField()
