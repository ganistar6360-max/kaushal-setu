from flask import Flask
from flask_cors import CORS
from routes.declaration import declaration_bp
from routes.assessment import assessment_bp
from routes.candidates import candidates_bp

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(declaration_bp)
app.register_blueprint(assessment_bp)
app.register_blueprint(candidates_bp)


@app.route("/")
def index():
    return {
        "app": "Kaushal Setu — AI-Assisted RPL Skill Assessment Tool",
        "status": "running",
        "note": "This tool is designed to SUPPORT an assessor's decision, not replace it. The assessor always has final override control.",
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
