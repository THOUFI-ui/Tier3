from flask import Blueprint, render_template
from app.models import Test

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    data = Test.query.all()
    return render_template("index.html", data=data)
