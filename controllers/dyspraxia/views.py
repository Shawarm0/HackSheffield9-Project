from flask import Blueprint, render_template

dyspraxia_bp = Blueprint("dyspraxia", __name__, template_folder="templates")


@dyspraxia_bp.route("/dyspraxia")
def dyspraxia():
    return render_template("dyspraxia/dyspraxia.html")
