from flask import Flask
from flask_ngrok import run_with_ngrok
import os

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def index():
    return '<h1>Hi  ^_^<h1>'


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(port=port)
