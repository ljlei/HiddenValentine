from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

class Valentine(FlaskForm):
    recipient = IntegerField('recipient', validators=[DataRequired(), NumberRange
                                                     (min=0, max=9, message="Please enter a number between 1-9!"),
                                                     Length(min=1, max=11)])
    message = StringField('message', validators=[DataRequired(), Length(min=-1, max=1600)])
    submit = SubmitField('submitted')

