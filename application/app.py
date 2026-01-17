from flask import Flask, request
from db import base, engine, session
import model


def create_app():
    app = Flask(__name__)
    base.metadata.create_all(engine)
    return app


app = create_app()


@app.route("/")
def home():
    return "hello"


@app.route('/signup', methods=['POST'])
def signup():
    req_data = request.json
    print("Sign", type(req_data))
    db = session()
    data = model.userdetails()
    data.email = req_data['user']
    data.password = req_data['password']

    db.add(data)
    db.commit()

    return "hwllo"


if __name__ == "__main__":
    app.run(debug=True)
