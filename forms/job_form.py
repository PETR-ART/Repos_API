from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField, IntegerField, StringField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = IntegerField("Айди", validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = IntegerField("Размер работы")
    collaborators = StringField("Колаборация")

    submit = SubmitField("Субмит")