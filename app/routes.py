# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        },
        {
            'author': {'username': 'jopa'},
            'body': 'Dima skazal pisat vesde "jopa"'
        }
    ]
    # ипортированная функкция рендеринга шаблонов  render_template.
    # Принимает имя файла шаблона, переменную, список аргументов.
    # Заменяет блоки {{ .. }} соответствующими значениями, заданными аргументами
    # указанными в вызове render_template().
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST']) # По факту добавляет
# часть ссылки, для перехода на страницу указанной в функции
# methods - объясняет, что фунция принимает эти запросы, а не только get
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Метод form.validate_on_submit() выполняет всю обработку формы.
        # Когда браузер отправляет запрос GET для получения веб-страницы с
        # формой, этот метод возвращает False, поэтому в этом случае функция
        # пропускает оператор if и переходит к отображению шаблона в последней
        # строке функции.
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
# Когда браузер отправляет запрос POST в результате нажатия пользователем кнопки
# submit, form.validate_on_submit() собирает все данные, запускает все валидаторы,
# прикрепленные к полям, и если все в порядке, вернет True, сообща что данные
# действительны и могут быть обработаны приложением. Но если хотя бы одно поле не
# подтвердит проверку, функция вернет False, и это приведет к тому, что форма будет
# возвращена пользователю, например, в случае запроса GET.