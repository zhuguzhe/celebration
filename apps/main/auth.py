from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/user', methods=['GET'])
def celebrate_user():
    return render_template("celebrations.html")