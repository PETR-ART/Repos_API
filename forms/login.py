from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    login = EmailField('Почта/Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')