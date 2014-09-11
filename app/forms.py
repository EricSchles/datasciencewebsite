
from flask import current_app
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, ValidationError,SelectField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo

class UniqueUser(object):
    def __init__(self, message="User exists"):
        self.message = message

    def __call__(self, form, field):
        if current_app.security.datastore.find_user(email=field.data):
            raise ValidationError(self.message)


validators = {
    'email': [
        Required(),
        Email(),
        UniqueUser(message='Email address is associated with '
                           'an existing account')
    ],
    'password': [
        Required(),
        Length(min=6, max=50),
        EqualTo('confirm', message='Passwords must match'),
        Regexp(r'[A-Za-z0-9@#$%^&+=]',
               message='Password contains invalid characters')
    ]
}


class RegisterForm(Form):
    email = TextField('Email', validators['email'])
    password = PasswordField('Password', validators['password'], )
    confirm = PasswordField('Confirm Password')


class WeeklyForm(Form):
    question_one = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_two = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_three = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_four = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_five = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_six = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_seven = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_eight = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_nine = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_ten = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_eleven = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_twelve = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_thirteen = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
    question_fourteen = SelectField('Response', choices=[('1','None of the time'),('2','Rarely'),('3','Some of the time'),('4','Often'),('5','All of the time')])
