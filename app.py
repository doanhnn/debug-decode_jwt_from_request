from flask import Flask,jsonify
from flask_jwt_extended.jwt_manager import JWTManager
from flask.globals import request
import AuthenService

jwt = JWTManager()
app = Flask(__name__)

app.config.from_pyfile("config.py")
jwt.init_app(app)

@app.route("/")
@AuthenService.authen
def home(**kwargs):
    return "Hello, Flask!"

app.run(debug=True)