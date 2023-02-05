from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length
import phonenumbers

class Valentine(FlaskForm):
    recipient = StringField('recipient', validators=[DataRequired(), Length(min=1, max=10)])
    valentine = StringField('valentine', validators=[DataRequired(), Length(min=1, max=55)])
    submit = SubmitField('Submit')

    def validate_phone(form, field):
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+1"+field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')