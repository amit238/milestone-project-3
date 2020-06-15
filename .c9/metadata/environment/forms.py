{"filter":false,"title":"forms.py","tooltip":"/forms.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":21,"column":36},"action":"insert","lines":["from flask_wtf import FlaskForm","from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField","from wtforms.validators import DataRequired, Length, EqualTo, Email","","","class LoginForm(FlaskForm):","    username = StringField('Username', validators=[DataRequired()])","    password = PasswordField('Password', validators=[DataRequired()])","    remember_me = BooleanField('Remember Me')","    submit = SubmitField('Sign In')","","","class RegisterForm(FlaskForm):","    username = StringField('Username', validators=[DataRequired(),","                                                   Length(min=4, max=20)])","    password = PasswordField('Password',","                             validators=[DataRequired(),","                                         EqualTo('password2', message='Passwords must match')])","    password2 = PasswordField('Repeat Password')","    email = StringField('Email Address', validators=[Length(min=6, max=35), Email()])","    remember_me = BooleanField('Remember Me')","    submit = SubmitField('Register')"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":27},"end":{"row":5,"column":27},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1592185171112,"hash":"ad9b443241c8810cc7f3065d6164c34b481c3861"}