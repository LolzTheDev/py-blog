# Author: LolzTheDev
# Version: 1.0.4
# GitHub: https://github.com/LolzTheDev/py-blog

from flask import Flask, render_template, request
from flask.logging import default_handler
import json, os, pymongo, datetime

os.system('clear||cls')

with open("./config.json") as config:
    config_contents = json.load(config)

    author = config_contents["author"]
    title = config_contents["title"]
    db_url = config_contents["mongodb_url"]
    debug_mode: bool = bool(config_contents["debug_mode"])

try:
    mongo = pymongo.MongoClient(db_url)
    db = mongo["blogdb"]
    posts = db["posts"]
except:
    print("Fatal database error. Exiting program.")

app = Flask(__name__)

# filter for unix timestamp -> formatted datetime string
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

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=8080, 
        debug=debug_mode
    )
