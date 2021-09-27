from flask import Flask, json, jsonify, request
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine


app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = "mongodb://localhost:27017/testflask"

db = MongoEngine()
db.init_app(app)

class Movie(db.Document):
    title = db.StringField()

@app.route('/add', methods=["POST"])
def add_test():
    body = request.get_json()
    movie = Movie(**body).save()
    return jsonify(movie), 201

@app.route("/", methods=["GET"])
def get_test():
    movie = Movie.objects()
    return jsonify(movie), 200

@app.route("/<id>", methods=["GET"])
def get_one_test(id:str):
    movie = Movie.objects(id=id).first()
    return jsonify(movie), 200


@app.route("/<id>", methods=["PUT"])
def update_one_test(id:str):
    body = request.get_json()
    movie = Movie.objects.get_or_404(id=id)
    movie.update(**body)
    return jsonify(body), 201

@app.route("/<id>", methods=["DELETE"])
def delete_one_test(id:str):
    movie = Movie.objects.get_or_404(id=id)
    movie.delete()
    return jsonify({
        "data":"Deleted!"
    })

app.run(port=4000)
