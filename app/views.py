from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
        return render_template("index.html")

@app.route('/webscraping_exercises')
def webscraping_exercises():
	return render_template("webscraping_exercises.html")
