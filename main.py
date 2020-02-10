# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import Response
import numpy as np
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import back

app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', nav_item="Главная")


@app.context_processor
def utility_processor():
    def is_active(item_name, current_name):
        return "active" if item_name == current_name else ""
    return dict(is_active=is_active)


@app.route('/map')
def map():
    return render_template('map.html', title='Map', nav_item="Карта")


@app.route('/analytics')
def analytics():
    return render_template('analytics.html', title='Analytics', nav_item="Аналитика", listPoints=back.get_points())


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
    return render_template('specVal.html', listPointsValue=back.get_measurements_by_id(str(ID)), date=back.get_date())


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
    axis.plot(xs, yh, "-b", label="Влажность")
    axis.plot(xs, yt, "-r", label="Температура")
    axis.plot(xs, ya, "-g", label="Кислотность")
    plt.xticks(xs, " ")
    axis.legend(loc="upper left")
    return fig


@app.route('/glob_graphic')
def glob_graphic():
    return render_template('glob_graphic.html')


@app.route('/plot_mid.png')
def plot_mid_png():
    fig = create_mid_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_mid_figure():
    listPointsValue = back.get_mid_value()
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = []
    yh = []
    yt = []
    ya = []
    for i in range(30):
        xs.append(listPointsValue[1][i])
        yh.append(listPointsValue[0][i][0])
        yt.append(listPointsValue[0][i][1])
        ya.append(listPointsValue[0][i][2])
    axis.plot(xs, yh, "-b", label="Влажность")
    axis.plot(xs, yt, "-r", label="Температура")
    axis.plot(xs, ya, "-g", label="Кислотность")
    plt.xticks(xs, " ")
    axis.legend(loc="upper left")
    return fig


@app.route('/field.png')
def field_png():
    fig = create_field_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_field_figure():
    BBox = (38.473225, 38.490792, 54.785954, 54.795505)
    tud = back.get_tud()
    longitudes = tud[0]
    latitudes = tud[1]
    fig, ax = plt.subplots(figsize=(12, 6))
    field_img = plt.imread('./static/field.png')
    ax.scatter(longitudes, latitudes, zorder=1, marker='^', alpha=1, c='r', s=50)
 #   ax.set_title('Plotting Spatial Data on Riyadh Map')
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    cur_axes = plt.gca()
    cur_axes.axes.get_xaxis().set_visible(False)
    cur_axes.axes.get_yaxis().set_visible(False)
    ax.imshow(field_img, zorder=0, extent=BBox, aspect='equal')

    return fig
