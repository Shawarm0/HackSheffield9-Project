from flask import Blueprint, render_template, request, jsonify
from .forms import ChatForm
from controllers.utils import send_to_gemini
from markdown import markdown

chat_bp = Blueprint("chat", __name__, template_folder="templates")


# Route for the chat page
@chat_bp.route("/chat", methods=["GET", "POST"])
def chat():
    form = ChatForm()
    # Initialize chat_history if it doesn't exist
    if "chat_history" not in request.form:
        chat_history = []
    else:
        chat_history = request.form.get("chat_history", [])

    if form.validate_on_submit():
        user_message = form.user_input.data
        previous_gemini_response = chat_history[-1]["gemini"] if chat_history else ""  # type: ignore

        # Prompt for Gemini including the user's latest message and Gemini's previous response
        prompt = f"You will receive the use r's message and your previous response. Here is the user's message: {user_message}. Here is your previous response: {previous_gemini_response}. Please respond thoughtfully."

        # Send to Gemini and retrieve response
        gemini_response = send_to_gemini(prompt, user_message)

        # Append responses to chat history
        chat_history.append({"user": markdown(user_message), "gemini": markdown(gemini_response)})  # type: ignore

    return render_template("chat/chat.html", form=form, chat_history=chat_history)
