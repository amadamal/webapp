import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome home M Ajay Kumar!"

@app.route('/how are you Ajay')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run()
