from flask import Flask
from controllers.dyspraxia.views import dyspraxia_bp

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)

app.config["WTF_CSRF_ENABLED"] = False

app.config["WTF_CSRF_ENABLED"] = False
app.config["UPLOAD_FOLDER"] = "images"

# blueprints config - routing
from controllers.dyspraxia.views import dyspraxia_bp
from controllers.dyslexia.views import dyslexia_bp
from controllers.dysgraphia.views import dysgraphia_bp
from controllers.dyscalculia.views import dyscalculia_bp
from controllers.chat.views import chat_bp
from controllers.autism.views import autism_bp

app.register_blueprint(dyspraxia_bp)
app.register_blueprint(dyslexia_bp)
app.register_blueprint(dysgraphia_bp)
app.register_blueprint(dyscalculia_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(autism_bp)
