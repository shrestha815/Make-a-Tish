from flask import Blueprint, render_template, request

register_blueprint = Blueprint('register', __name__, template_folder='templates')

@register_blueprint.route('/register/', methods = ["GET"])
def register():
    return render_template("register.html")