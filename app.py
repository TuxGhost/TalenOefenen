from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    name = "Mirthe"
    return render_template('index.html', title='Welcome', username = name)
    #return 'Web app with python Flask!'

app.run(host='0.0.0.0', port=9001)