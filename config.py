from flask import Flask
from controllers.dyspraxia.views import dyspraxia_bp

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)

# I dont actually know if we need the UPLOAD_FOLDER variable but im keeping it anyway in case it breaks something. 
app.config["UPLOAD_FOLDER"] = "images"
app.config["WTF_CSRF_ENABLED"] = False

# blueprints config - routing
from controllers.dyspraxia.views import dyspraxia_bp
from controllers.dyslexia.views import dyslexia_bp
from controllers.dysgraphia.views import dysgraphia_bp
from controllers.motor.views import motor_bp
from controllers.chat.views import chat_bp
from controllers.autism.views import autism_bp

app.register_blueprint(dyspraxia_bp)
app.register_blueprint(dyslexia_bp)
app.register_blueprint(dysgraphia_bp)
app.register_blueprint(motor_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(autism_bp)
