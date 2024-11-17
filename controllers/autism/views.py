from flask import Blueprint, render_template, request, jsonify
from controllers.autism.forms import AutismForm
from controllers.utils import send_to_gemini

autism_bp = Blueprint("autism", __name__, template_folder="templates")  

# Route to handle autism text input and processing
@autism_bp.route("/autism", methods=["GET", "POST"])
def autism():
    if request.method == "POST" and request.is_json:  # Handle AJAX POST request
        data = request.get_json()
        user_text = data.get("text", "")

        if not user_text.strip():
            return jsonify({"error": "No input text provided"}), 400

        # Process the input text using the Gemini API
        processed_text = send_to_gemini(
            "Translate the following text in a way that replaces any slang or idioms with their actual meanings, making it easier for an autistic person to understand:",
            user_text
        )

        return jsonify({"processed_text": processed_text})  # Return JSON response

    # Render the form on GET request
    form = AutismForm()
    return render_template("autism/autism.html", form=form, output=None)
