from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
import wtforms as wf
from werkzeug.utils import secure_filename

from . import app
from .models import Transactions, User

class TransactionsForm(FlaskForm):
    period = wf.StringField(label="Период", validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=60)
    ])
    value = wf.IntegerField(label='Сумма', validators=[
        wf.validators.DataRequired()
    ])
    status = wf.StringField(label='Статус', validators=[
        wf.validators.DataRequired()
    ])
    unit = wf.StringField(label='Валюта', validators=[
        wf.validators.DataRequired()
    ])
    subject = wf.TextAreaField(label="Комментарии", validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=255)
    ])


class TransactionsUpdateForm(FlaskForm):
    period = wf.StringField(label="Период", validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=60)
    ])
    value = wf.IntegerField(label='Сумма', validators=[
        wf.validators.DataRequired()
    ])
    status = wf.StringField(label='Статус', validators=[
        wf.validators.DataRequired()
    ])
    unit = wf.StringField(label='Валюта', validators=[
        wf.validators.DataRequired()
    ])
    subject = wf.TextAreaField(label="Комментарии", validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=255)
    ])


class UserLoginForm(FlaskForm):
    username = wf.StringField(label='Логин', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=20)
    ])
    password = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired()
    ])

    def validate_password(self, field):
        if len(field.data) < 8:
            raise wf.ValidationError('Длина пароля должна быть минимум 8 символов')

class UserRegisterForm(UserLoginForm):
    password_2 = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired()
    ])

    def validate(self, *args, **kwargs):
        if not super().validate(*args, **kwargs):
            return False
        if self.password.data != self.password_2.data:
            self.password_2.errors.append('Пароли должны совпадать')
            return False
        return True

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).count() > 0:
            raise wf.ValidationError('Пользователь с таким username уже существует')


