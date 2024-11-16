from flask import Blueprint, render_template


dysgraphia_bp = Blueprint("dysgraphia", __name__, template_folder="templates")


@dysgraphia_bp.route("/dysgraphia")
def dysgraphia():
    return render_template("dysgraphia/dysgraphia.html")
