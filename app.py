from flask import Flask
from routes.student_routes import student_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(student_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
