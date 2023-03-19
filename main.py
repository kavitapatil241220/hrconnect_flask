from flask import Flask, render_template
from task_one import get_data_info
app = Flask(__name__)


@app.route('/')
def index():
    return "welcome flask programming"

@app.route("/welcome")
def welcome():
    return render_template("index.html")


@app.route("/task_one")
def call_task_one():
    return render_template("taskone.html", emp_data=get_data_info())


