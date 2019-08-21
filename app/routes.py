# -*- coding: utf-8 -*-
from flask import render_template
from app import app


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


