from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class Valentine(FlaskForm):
    recipient = StringField('recipient', validators=[DataRequired(), Length(min=1, max=10)])
    valentine = StringField('valentine', validators=[DataRequired(), Length(min=-1, max=1600)])
    submit = SubmitField('Submit')