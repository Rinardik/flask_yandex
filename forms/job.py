from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job_title = StringField('Название работы', validators=[DataRequired()])
    team_leader_id = IntegerField('ID руководителя', validators=[DataRequired()])  # Теперь это просто число
    work_size = IntegerField('Объем работы (часы)', validators=[DataRequired()])
    collaborators = TextAreaField('Участники (через запятую)')
    is_finished = BooleanField('Работа завершена')
    submit = SubmitField('Добавить работу')