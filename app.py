from datetime import datetime
from flask import Flask, render_template
import json
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__)

@app.route('/')
def index():
    with open('config/context.json') as f:
        context = json.load(f)
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("index.html.jinja2")

    ## FOR CONTACT US PAGE, ADD DROPDOWN FOR SUBJECT LINE, INQUIRY VS SUPPORT

    output = template.render(**context)

    return output

@app.route('/privacy')
def privacy():
    with open('config/context.json') as f:
        context = json.load(f)
    
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("privacy.html.jinja2")

    ## FOR CONTACT US PAGE, ADD DROPDOWN FOR SUBJECT LINE, INQUIRY VS SUPPORT

    output = template.render(**context)

    return output

if __name__ == '__main__':
    app.run(debug=True)
