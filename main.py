import flask
import json
import os

from werkzeug.middleware.proxy_fix import ProxyFix

app = flask.Flask(__name__)

# App is behind one proxy that sets the -For and -Host headers.
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_host=1
)

@app.route("/")
def home():
    return flask.render_template("index.html")

POSTS = "../Data/Kaffe/forum.json"
 
@app.route('/forum/submit', methods=['POST'])
def process_form():
    rubrik = flask.request.form.get('rubrik')
    text = flask.request.form.get('text')
    namn = flask.request.form.get('namn')
    
    with open(POSTS, "a") as file:
        file.write(json.dumps({
            "rubrik": rubrik,
            "text": text,
            "namn": namn
        }) + "\n")
    
    return flask.redirect("/forum")
 
@app.route("/forum")
def page():
    with open(POSTS) as file:
        return flask.render_template(f"forum.html",
            data=[json.loads(line) for line in file.read().splitlines()]
        )
        
@app.route("/kaffepress")
def kaffepress():
    return flask.render_template("kaffepress.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
