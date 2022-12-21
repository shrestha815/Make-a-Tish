from flask import Blueprint, render_template, request

checkout_signed_out_blueprint = Blueprint('checkout_signed_out', __name__, template_folder='templates')

@checkout_signed_out_blueprint.route('/checkout_signed_out/', methods = ["GET"])
def editor():
    return render_template("checkout_signed_out.html")