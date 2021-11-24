# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, фласк"


app.run()
