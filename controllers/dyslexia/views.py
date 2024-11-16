from flask import Blueprint, render_template

dyslexia_bp = Blueprint("dyslexia", __name__, template_folder="templates")


@dyslexia_bp.route("/dyslexia")
def dyslexia():
    return render_template("dyslexia/dyslexia.html")
