from flask import Blueprint, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager

main = Blueprint("main", __name__)
jwt = JWTManager()
cors = CORS(resources={r"/*":{"origins":"*"}})


@main.route("/")
def home():
    return render_template("index.html")
