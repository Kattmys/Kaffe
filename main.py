import flask
import json
import time
from datetime import datetime

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")

# POSTS = "../Data/Kaffe/forum.json"
POSTS = "forum.json"
 
@app.route('/forum/submit', methods=['POST'])
def process_form():
    rubrik = flask.request.form.get('rubrik')
    text = flask.request.form.get('text')
    namn = flask.request.form.get('namn')
    unix = time.time()
    
    with open(POSTS, "a") as file:
        file.write(json.dumps({
            "rubrik": rubrik,
            "text": text,
            "namn": namn,
            "unix": unix,
        }) + "\n")
    
    return flask.redirect("/forum")
 
@app.route("/forum")
def page():
    with open(POSTS) as file:
        data = [json.loads(line) for line in file.read().splitlines()]
        for inlägg in data:
            inlägg["klartid"] = datetime.fromtimestamp(inlägg["unix"]).isoformat(" ", "seconds")
        return flask.render_template(f"forum.html",
            data=data
        )
        
@app.route("/kaffepress")
def kaffepress():
    return flask.render_template("kaffepress.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
