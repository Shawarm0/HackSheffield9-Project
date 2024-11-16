from flask import Blueprint, render_template

from controllers.dyslexia.forms import DyslexiaForm

dyslexia_bp = Blueprint("dyslexia", __name__, template_folder="templates")


@dyslexia_bp.route("/dyslexia")
def dyslexia():
    form = DyslexiaForm()

    if not form.validate_on_submit():
        return render_template("dyslexia/dyslexia.html", form=form)

    return render_template("dyslexia/dyslexia.html")
