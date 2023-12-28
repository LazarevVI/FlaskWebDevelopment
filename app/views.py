from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    user = {"login": "Constantine", "email": "const@gmail.com"}
    return render_template("index.html", title = "Home", user = user)