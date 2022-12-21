from flask import Blueprint, render_template, request

checkout_blueprint = Blueprint('checkout', __name__, template_folder='templates')

@checkout_blueprint.route('/checkout/', methods = ["GET"])
def editor():
    return render_template("checkout.html")