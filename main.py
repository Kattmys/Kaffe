import flask
import json

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("index.html")
 
@app.route('/forum/submit', methods=['POST'])
def process_form():
    rubrik = flask.request.form.get('rubrik')
    text = flask.request.form.get('text')
    namn = flask.request.form.get('namn')
    
    with open("data.json", "a") as file:
        file.write(json.dumps({
            "rubrik": rubrik,
            "text": text,
            "namn": namn
        }) + "\n")
    
    return flask.redirect("/forum")
 
@app.route("/forum")
def page():
    with open("data.json") as file:
        return flask.render_template(f"forum.html",
            data=[json.loads(line) for line in file.read().splitlines()]
        )
        
@app.route("/kaffepress")
def kaffepress():
    return flask.render_template("kaffepress.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, ssl_context=('/etc/letsencrypt/live/kattmys.se/fullchain.pem', '/etc/letsencrypt/live/kattmys.se/privkey.pem'))