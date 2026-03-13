from datetime import datetime
from flask import Flask, render_template, url_for
import json
from jinja2 import Environment, FileSystemLoader
from flask_frozen import Freezer

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build' # The output directory
freezer = Freezer(app)

@app.route('/')
def index():
    with open('config/context.json') as f:
        context = json.load(f)
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("index.html.jinja2")

    output = template.render(**context)

    return output

@app.route('/privacy.html')
def privacy():
    with open('config/context.json') as f:
        context = json.load(f)
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("privacy.html.jinja2")

    output = template.render(**context)

    return output


@app.route('/about.html')
def about():
    with open('config/context.json') as f:
        context = json.load(f)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("about.html.jinja2")

    output = template.render(**context)

    return output


@app.route('/faq.html')
def faq():
    with open('config/context.json') as f:
        context = json.load(f)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("faq.html.jinja2")

    output = template.render(**context)

    return output


# Add a freezer generator for all routes
@freezer.register_generator
def url_generator():
    yield url_for('index')
    yield url_for('privacy')
    yield url_for('about')
    yield url_for('faq')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--freeze', action='store_true')
    args = parser.parse_args()

    if args.freeze:
        freezer.freeze()
    else:
        app.run(debug=True)
