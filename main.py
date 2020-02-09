# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import repository

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Эльдар Рязанов'}
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
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.context_processor
def utility_processor():
    def is_active(item_name, current_name):
        return "active" if item_name == current_name else ""
    return dict(is_active=is_active)


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/analytics')
def analytics():
    return render_template('analytics.html', listPoints=repository.get_points_all())


@app.route('/whatitis')
def what_it_is():
    return render_template('whatitis.html')


@app.route('/hwwt')
def hwwt():
    return render_template('hwwt.html')


@app.route('/faq')
def faq():
    return render_template('FAQ.html')


@app.route('/specVal')
def special_value():
    ID = request.args.get('ID')
    return render_template('specVal.html', listMeasurements=repository.get_measurements_by_id(str(ID)), point_id=ID)
