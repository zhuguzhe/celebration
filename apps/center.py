from flask import Blueprint, render_template

centers = Blueprint('center', __name__)


@centers.route('/', methods=['GET'])
def celebrate_user():
    return render_template("center.html", title='人生导师', name='王建')