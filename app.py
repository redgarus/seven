from flask import Flask, render_template, redirect
import re

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def redirected():
	return redirect("/home")


@app.route('/home')
def index():
	return render_template("main.html")


@app.route('/students')
def pupils():
	return render_template("students.html")


@app.route('/teachers')
def teacher():
	return render_template("teachers.html")


@app.route('/dnevnik')
def dnevnik():
	return render_template("dnevnik.html")


if __name__ == "__main__":
	app.run(debug=True)
