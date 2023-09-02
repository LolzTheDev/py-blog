# Author: LolzTheDev
# Version: 1.0.0
# GitHub: https://github.com/LolzTheGreat/py-blog

from flask import Flask, render_template
import json, os, pymongo, datetime

os.system('clear||cls')

with open("./config.json") as config:
    config_contents = json.load(config)

    author = config_contents["author"]
    title = config_contents["title"]
    db_url = config_contents["mongodb_url"]

mongo = pymongo.MongoClient(db_url)
db = mongo["blogdb"]
posts = db["posts"]

app = Flask(__name__)

# filter for unix timestamp -> datetime obj
@app.template_filter('utod')
def utod(uts):
    return datetime.datetime.fromtimestamp(uts).strftime("%m/%d/%Y, %I:%M:%S %p")

@app.route("/", methods=["GET"])
def home():
    # find and sort posts by time | uses unix timestamps
    _posts = posts.find({ "author" : author }).sort('date', pymongo.DESCENDING)

    return render_template(
        "home.html", 
        page_title=title, 
        posts=_posts, 
        author=author
    )

app.run("0.0.0.0", 8080)