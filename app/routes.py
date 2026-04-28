from flask import Blueprint, render_template
from .models import Test

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    data = Test.query.all()
    return render_template("index.html", data=data)
