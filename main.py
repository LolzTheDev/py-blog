# Author: LolzTheDev
# Version: 1.0.0
# GitHub: https://github.com/LolzTheGreat/py-blog

from flask import Flask, render_template
import json, os, pymongo

os.system('clear||cls')

with open("./config.json") as config:
    author = json.load(config)["author"]
    title = json.load(config)["title"]
    db_url = json.load(config)["mongodb_url"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", page_title=title)

app.run("0.0.0.0", 8080)