# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import Response
import numpy as np
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
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
    return render_template('index.html', title='Home', nav_item="gl")


@app.context_processor
def utility_processor():
    def is_active(item_name, current_name):
        return "active" if item_name == current_name else ""
    return dict(is_active=is_active)


@app.route('/map')
def map():
    return render_template('map.html', title='Map', nav_item="gl")


@app.route('/analytics')
def analytics():
    return render_template('analytics.html', title='Analytics', nav_item="gl", listPoints=back.get_points())


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
    return render_template('specVal.html', listPointsValue=back.get_measurements_by_id(str(ID)))


@app.route('/graphics')
def graphics():
    ID = request.args.get('ID')
    return render_template('graphics.html', ID=ID)


@app.route('/plot.png')
def plot_png():
    ID = request.args.get('ID')
    fig = create_figure(ID)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure(ID):
    listPointsValue = back.get_measurements_by_id(str(ID))[0]
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = []
    yh = []
    yt = []
    ya = []
    for pv in listPointsValue:
        xs.append(pv[0])
        yh.append(pv[1][0])
        yt.append(pv[1][1])
        ya.append(pv[1][2])
    axis.plot(xs, yh, xs, yt, xs, ya)
    return fig
