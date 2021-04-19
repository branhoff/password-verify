import re
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class ContainsLetter(object):
    def __init__(self, min_count=1, message=None):
        self.min_count = min_count
        if not message:
            message = u'Field must contain at least one letter'
        self.message = message

    def __call__(self, form, field):
        if not re.search(f'[a-zA-Z]', field.data):
            raise ValidationError(self.message)

class ContainsDigit(object):
    def __init__(self, min_count=1, message=None):
        self.min_count = min_count
        if not message:
            message = u'Field must contain at least one digit'
        self.message = message

    def __call__(self, form, field):
        if not re.search(f'[0-9]', field.data):
            raise ValidationError(self.message)

class RegistrationForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8), 
                                                     ContainsLetter(), ContainsDigit()])
    submit = SubmitField('Submit')
    
