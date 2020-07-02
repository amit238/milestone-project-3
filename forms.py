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
    
    genre = SelectField(u'Genre', choices=[
        ('Action/Adventure', 'Action/Adventure'),
        ('Sports', 'Sports'),
        ('Shooters', 'Shooters'),
        ('Role-playing', 'Role-Playing'),
        ('Racing', 'Racing'),
        ])
    
    rating = SelectField(u'Rating', choices=[
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ])
    
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=1500)])
    
    submit_add = SubmitField('Add Review')
    submit_edit = SubmitField('Update Review')