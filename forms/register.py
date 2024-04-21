from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login = EmailField('Логин/Емаил', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeat_password = PasswordField('Повтор пароль', validators=[DataRequired()])
    surname = StringField('Фамилия')
    name = StringField('Имя')
    age = IntegerField('Возраст')
    submit = SubmitField('Войти')