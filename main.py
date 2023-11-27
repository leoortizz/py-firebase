# Entry point for the application.
# from . import app    # For application discovery by the 'flask' command. 
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# from . import views  # For import side-effects of setting up routes. 

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
