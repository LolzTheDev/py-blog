# Author: LolzTheDev
# Version: 1.0.4
# GitHub: https://github.com/LolzTheDev/py-blog

from flask import Flask, render_template, request, redirect
from flask.logging import default_handler
from bson.objectid import ObjectId
from bson import json_util
import json, os, pymongo, datetime, time, bson.errors

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
start_time = time.time()

# filter for unix timestamp -> formatted datetime string
@app.template_filter('utod')
def utod(uts):
    return datetime.datetime.fromtimestamp(uts).strftime("%m/%d/%Y, %I:%M:%S %p")

@app.route("/", methods=["GET"])
@app.route("/<dev_mode>", methods=["GET"])
def home(dev_mode=False):
    if str(dev_mode).lower() == "true" or str(dev_mode).lower == "false":
        # find and sort posts by time | uses unix timestamps
        _posts = posts.find({ "author" : author }).sort('date', pymongo.DESCENDING)

        return render_template(
            "home.html", 
            page_title=title, 
            posts=_posts, 
            author=author,
            dev_mode=dev_mode
        )
    else:
        return redirect("/")

# api to GET posts
@app.route("/api/", methods=["GET"])
def api_home():
    return json.loads(json.dumps({
        'uptime': int(time.time() - start_time),
        'stats': {
            'post_count': posts.count_documents({})
        }
    }))

@app.route("/api/posts/", methods=["GET"])
def api_all_posts():
    _posts = list(posts.find({}))
    return json.loads(json_util.dumps(_posts))

@app.route("/api/post/<id>", methods=["GET"])
def api_post(id=None):
    if id == None:
        return redirect("/api/")
    else:
        try:
            if posts.count_documents({"_id" : ObjectId(id)}) > 0:
                _post = posts.find_one({"_id" : ObjectId(id)})

                return json.loads(json.dumps({
                    'title': _post["title"],
                    'content': _post["content"],
                    'author': _post["author"],
                    'timestamp': _post["date"],
                    "id": _post["_id"]
                }, default=str))
            else:
                return json.loads(json.dumps({
                    'error': {
                        'code': 404,
                        'msg': 'post not found'
                    }
                }))
        except bson.errors.InvalidId as InvalidIdErr:
            return json.loads(json.dumps({
                    'error': {
                        'code': 404,
                        'msg': 'post not found (invalid id?)'
                    }
                }))


if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=8080, 
        debug=debug_mode
    )
