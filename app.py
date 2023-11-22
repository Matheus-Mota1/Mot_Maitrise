from flask import Flask, render_template, request
import database

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", message="Welcome to Mot Matrîse")