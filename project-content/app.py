from flask import Flask, render_template, request, url_for

from routes.register import register_blueprint
from routes.editor import editor_blueprint
from routes.checkout import checkout_blueprint
from routes.checkout_signed_out import checkout_signed_out_blueprint

app = Flask(__name__)
app.register_blueprint(register_blueprint)
app.register_blueprint(editor_blueprint)
app.register_blueprint(checkout_blueprint)
app.register_blueprint(checkout_signed_out_blueprint)

@app.route("/", methods= ["GET"])
def index():
    return render_template("index.html")

@app.route('/sign_in/', methods = ["GET"])
def signin():
    return render_template("sign_in.html")

@app.route('/explore/', methods = ["GET"])
def explore():
    return render_template("explore.html")

@app.route('/homeUser/', methods = ["GET"])
def homeUser():
    return render_template("homeUser.html")

@app.route('/about_user/', methods = ["GET"])
def about_user():
    return render_template("exploreUser.html")

@app.route('/editor_signedout/', methods = ["GET"])
def editor_signedout():
    return render_template("editor_logout.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost")