from db import BaseClass, Session, Engine
from flask import Flask, jsonify
import model
from auth.signup import signup_app
from auth.login import login_blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    BaseClass.metadata.create_all(Engine)
    app.register_blueprint(signup_app)
    app.register_blueprint(login_blueprint)
    return app


app = create_app()


@app.route("/")
def health_check():
    return jsonify({
        "status": "Running"
    })


if __name__ == "__main__":
    app.run(debug=True)
