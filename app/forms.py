'''Расширение Flask-WTF использует классы Python для представления веб-форм.
Класс формы просто определяет поля формы как переменные класса.

Еще раз имея в виду разделение проблем, я собираюсь использовать новый
app/forms.py модуль для хранения классов веб-форм.'''


from flask_wtf import FlaskForm #для обработки вебформ, обертка WTForms for Flask
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


# Четыре класса, которые представляют типы полей, которые я использую для этой
# формы, импортируются непосредственно из пакета WTForms, поскольку расширение
# Flask-WTF не предоставляет настраиваемые версии. Для каждого поля объект
# создается как переменная класса в классе LoginForm. Каждому полю присваивается
# описание или метка в качестве первого аргумента.
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # Валидатор DataRequired - проверяет что поле не отправлено пустым
    # есть разные валидаторы
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')