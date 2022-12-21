from flask import Blueprint, render_template, request

editor_blueprint = Blueprint('editor', __name__, template_folder='templates')

@editor_blueprint.route('/editor/', methods = ["GET"])
def editor():
    return render_template("editor.html")