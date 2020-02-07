# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import flash
import back

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


@app.route('/map')
def map():
    flash("flash test!!!!")
    flash("flash test!!!!")
    flash("flash test!!!!")
    flash("flash test!!!!")
    return render_template('map.html')


@app.route('/analytics')
def analytics():
    return render_template('analytics.html', listPoints=back.add_points())


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
    return render_template('specVal.html', listPointsValue=back.add_points_value())

