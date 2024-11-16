from flask import Blueprint, render_template


dyscalculia_bp = Blueprint("dyscalculia", __name__, template_folder="templates")


@dyscalculia_bp.route("/dyscalculia")
def dyscalculia():
    return render_template("dyscalculia/dyscalculia.html")
