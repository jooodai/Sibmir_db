from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Логин:', validators=[DataRequired()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    remember_me = BooleanField('Запомни меня')
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    fio = StringField('ФИО:', validators=[DataRequired()])
    department = SelectField('Отдел:', choices=[(' ', ' '),
                                               ('АУП', 'АУП'),
                                               ('Отдел АСУТП и ТМ','Отдел АСУТП и ТМ'),
                                               ('Отдел проектной и конструкторской документации', 'Отдел проектной и конструкторской документации'),
                                               ('Отдел управления проектами','Отдел управления проектами'),
                                               ('Склад','Склад')
                                               ])
    problem = SelectField('Выполняемые задачи:', choices=[(' ', ' '),
                                               ('Проектирование', 'Проектирование'),
                                               ('Конструирование','Конструирование'),
                                               ('Руководитель ПКД', 'Руководитель ПКД'),
                                               ('Закупка','Закупка'),
                                                ('Тестирование оборудования ', 'Тестирование оборудования'),
                                                ('Сборка в производстве', 'Сборка в производстве'),
                                                ('Директор производства', 'Директор производства'),
                                                ('Директор Чебоксарского подразделения', 'Директор Чебоксарского подразделения'),
                                                ('Инженер отдела АСУТП', 'Инженер отдела АСУТП'),
                                               ('Кладовщик','Кладовщик'),
                                                ('Сметчик', 'Сметчик')
                                               ])
    place = StringField('Должность:', validators=[DataRequired()])
    username = StringField('Логин:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста используйте другой логин')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Пожалуйста используйте другой адрес Email')


class RegistrationNewElement(FlaskForm):
    name_element = StringField('Наименование:', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
