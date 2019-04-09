# main.py

from flask import Flask

app = Flask(__name__)

@app.route('/index.html')
def index():
    return index.html

app.run()
