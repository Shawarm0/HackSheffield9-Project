from flask import Blueprint, render_template


motor_bp = Blueprint("motor", __name__, template_folder="templates")


@motor_bp.route("/motor")
def motor():
    return render_template("motor/motor.html")
