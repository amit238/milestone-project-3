from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=4, max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Repeat Password')
    email = StringField('Email Address', validators=[Length(min=6, max=35), Email()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Register')
    

class ReviewGameForm(FlaskForm):

    user_created = StringField('User Created', validators=[DataRequired(), Length(min=1, max=100)])
    
    name = StringField('Name', validators=[DataRequired(),Length(min=1, max=150)])
    
    rating = TextAreaField('Rating', validators=[DataRequired(), Length(min=0, max=2)])
    
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=1500)])
    
    genre = SelectField(u'Genre', choices=[
        ('action/adventure', 'Action/Adventure'),
        ('sports', 'Sports'),
        ('shooters', 'Shooters'),
        ('role-playing', 'Role-Playing'),
        ('racing', 'Racing'),
        ])
    
    submit_add = SubmitField('Add Review')