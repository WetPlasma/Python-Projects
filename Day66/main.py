from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///D:\\Shreyas\\python tutorials\\66ApiCreation\\cafes.db"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


@app.route("/random", methods=["GET"])
def get_random_cafe():
    if request.method == "GET":
        cafe = db.session.query(Cafe).all()
        random_cafe = random.choice(cafe)
        return jsonify(
            {
                "cafe": {
                    "name": random_cafe.name,
                    "map_url": random_cafe.map_url,
                    "img_url": random_cafe.img_url,
                    "location": random_cafe.location,
                    "seats": random_cafe.seats,
                    "has_toilet": random_cafe.has_toilet,
                    "has_wifi": random_cafe.has_wifi,
                    "has_sockets": random_cafe.has_sockets,
                    "can_take_calls": random_cafe.can_take_calls,
                    "coffee_price": random_cafe.coffee_price,
                }
            }
        )


@app.route("/all", methods=["GET"])
def get_all_cafes():
    if request.method == "GET":
        cafes = db.session.query(Cafe).all()
        cafe_list = []
        for cafe in cafes:
            cafe_list.append(
                {
                    "id": cafe.id,
                    "name": cafe.name,
                    "map_url": cafe.map_url,
                    "img_url": cafe.img_url,
                    "location": cafe.location,
                    "seats": cafe.seats,
                    "has_toilet": cafe.has_toilet,
                    "has_wifi": cafe.has_wifi,
                    "has_sockets": cafe.has_sockets,
                    "can_take_calls": cafe.can_take_calls,
                    "coffee_price": cafe.coffee_price,
                }
            )
        return jsonify(cafe_list)


@app.route("/search", methods=["GET"])
def search_cafe():
    if request.method == "GET":
        location = request.args.get("loc")
        if not location:
            return jsonify({"error": "No cafes found for that location"})
        else:
            cafes = db.session.query(Cafe).filter_by(location=location).all()
            cafe_list = []
            for cafe in cafes:
                cafe_list.append(
                    {
                        "id": cafe.id,
                        "name": cafe.name,
                        "map_url": cafe.map_url,
                        "img_url": cafe.img_url,
                        "location": cafe.location,
                        "seats": cafe.seats,
                        "has_toilet": cafe.has_toilet,
                        "has_wifi": cafe.has_wifi,
                        "has_sockets": cafe.has_sockets,
                        "can_take_calls": cafe.can_take_calls,
                        "coffee_price": cafe.coffee_price,
                    }
                )
            return jsonify(cafe_list)


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)

    if not cafe:
        return (
            jsonify({"error": "No cafe found with that ID"}),
            404,
        )  # Return 404 if not found

    new_price = request.json.get("new_price")  # Handle JSON payload properly
    if not new_price:
        return (
            jsonify({"error": "New price is required"}),
            400,
        )  # Return 400 if no new_price is provided

    cafe.coffee_price = new_price
    db.session.commit()

    return (
        jsonify(response={"success": "Successfully updated the price."}),
        200,
    )  # Return 200 OK


@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)

    if not cafe:
        return (
            jsonify({"error": "No cafe found with that ID"}),
            404,
        )  # Return 404 if not found

    api_key = request.args.get("api-key")  # Handle JSON payload correctly
    if api_key != "TopSecretAPIKey":
        return (
            jsonify(
                {
                    "error": "Sorry, that's not allowed. Make sure you have the correct API key."
                }
            ),
            403,
        )  # Return 403 Forbidden

    db.session.delete(cafe)
    db.session.commit()

    return (
        jsonify(response={"success": "Successfully deleted the cafe."}),
        200,
    )  # Return 200 OK


if __name__ == "__main__":
    app.run(debug=True)
