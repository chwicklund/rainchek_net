from datetime import datetime
from flask import Flask, render_template
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

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    # Use the freezer if run directly
    freezer.freeze()