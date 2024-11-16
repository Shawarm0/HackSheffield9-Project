from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


# blueprints config - routing
from controllers.dyspraxia.views import dyspraxia_bp
from controllers.dyslexia.views import dyslexia_bp
from controllers.dysgraphia.views import dysgraphia_bp
from controllers.dyscalculia.views import dyscalculia_bp

app.register_blueprint(dyspraxia_bp)
app.register_blueprint(dyslexia_bp)
app.register_blueprint(dysgraphia_bp)
app.register_blueprint(dyscalculia_bp)
