import flask
import json
import time
from datetime import datetime
import os

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")

POSTS = "../Data/Kaffe/forum.json"
DATA  = "../Data/Kaffe/data.json"
 
@app.route('/forum/submit', methods=['POST'])
def process_form():
    rubrik = flask.request.form.get('rubrik')
    text = flask.request.form.get('text')
    namn = flask.request.form.get('namn')
    unix = time.time()

    with open(DATA) as file:
        data = json.load(file)
    id_ = data["next_id"]
    data["next_id"] += 1
    with open(DATA, "w") as file:
        json.dump(data, file)
    
    with open(POSTS) as file:
        posts = json.load(file)

    posts[str(id_)] = {
        "rubrik": rubrik,
        "text": text,
        "namn": namn,
        "unix": unix,
    }

    with open(POSTS, "w") as file:
        json.dump(posts, file)
    
    return flask.redirect("/forum")
 
@app.route("/forum")
def page():
    with open(POSTS) as file:
        data = json.load(file)

    posts = []

    for id_ in data:
        inlägg = data[id_]
        inlägg["id"] = id_
        if "unix" in inlägg:
            inlägg["klartid"] = datetime.fromtimestamp(inlägg["unix"]).isoformat(" ", "seconds")
        posts.append(inlägg)

    return flask.render_template(f"forum.html",
        data=posts
    )
        
@app.route("/kaffepress")
def kaffepress():
    return flask.render_template("kaffepress.html")

if __name__ == "__main__":
    POSTS = "forum.json"
    DATA  = "data.json"
    app.run(host="127.0.0.1", port=5000)
