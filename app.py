from flask import Flask, jsonify, request
from Models import db, Plants
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database/plants.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False
db.init_app(app)


#Aquí empiezan las rutas
@app.route("/")
def home():
    return "<h1>Welcome home</h1>"


@app.route("/api/plants", methods=["GET"])
def getPlants():
    try:
        
        plants = Plants.query.all()
        toReturn = [plant.serialize() for plant in plants]
        return jsonify(toReturn), 200

    except Exception:
        
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@app.route("/api/plant", methods=["GET"])
def getPlantByName():
    try:
        titlePlant = request.args["title"]
        plant = Plants.query.filter_by(title=titlePlant).first()
        if not plant:
            return jsonify({"msg": "Esta planta no está en la lista"}), 200
        else:
            return jsonify(plant.serialize()), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500
    
@app.route("/api/plant/<int:id>", methods=["GET"])
def getPlantById(id):
    try:
        plant = Plants.query.get(id)
        if not plant:
            return jsonify({"msg": "Esta planta no está en la lista"}), 200
        else:
            return jsonify(plant.serialize()), 200
    except Exception as e:
        print("[SERVER]: Error ->", e)
        return jsonify({"msg": "Ha ocurrido un error"}), 500

@app.route("/api/plant/<string:soil>", methods=["GET"])
def getPlantsBySoil(soil):
    try:
        plants = Plants.query.filter_by(soil=soil).all()
        if not plants:
            return jsonify({"msg": f"No hay plantas asociadas al tipo de suelo '{soil}'"}), 404
        else:
            return jsonify([plant.serialize() for plant in plants]), 200
    except Exception as e:
        exception("[SERVER]: Error ->", e)
        return jsonify({"msg": "Ha ocurrido un error"}), 500



@app.route("/api/findplant", methods=["GET"])
def getPlant():
    try:
        fields = {}
        if "id" in request.args:
            fields["id"] = request.args["id"]

        if "title" in request.args:
            fields["title"] = request.args["title"]

        if "description" in request.args:
            fields["description"] = request.args["description"]

        if "descriptionEnvironment" in request.args:
            fields["descriptionEnvironment"] = request.args["descriptionEnvironment"]

        if "image" in request.args:
            fields["image"] = request.args["image"]

        if "invasive" in request.args:
            fields["invasive"] = request.args["invasive"]
        
        if "native" in request.args:
            fields["native"] = request.args["native"]

        if "exotic" in request.args:
            fields["exotic"] = request.args["exotic"]

        if "caracteristic" in request.args:
            fields["caracteristic"] = request.args["caracteristic"]

        if "soil" in request.args:
            fields["soil"] = request.args["soil"]

        if "prados" in request.args:
            fields["prados"] = request.args["prados"]

        if "campos" in request.args:
            fields["campos"] = request.args["campos"]
        
        if "jardines" in request.args:
            fields["jardines"] = request.args["jardines"]

        if "costa" in request.args:
            fields["costa"] = request.args["costa"]

        if "interior" in request.args:
            fields["interior"] = request.args["interior"]

        if "montaña" in request.args:
            fields["montaña"] = request.args["montaña"]

        if "otros" in request.args:
            fields["otros"] = request.args["otros"]

        plant = Plants.query.filter_by(**fields).all()
        if not plant:
            return jsonify({"msg": "Esta planta no está en la lista"}), 200
        else:
            return jsonify(plant.serialize()), 200
    except Exception:
        exception("[SERVER]: Error ->")
        return jsonify({"msg": "Ha ocurrido un error"}), 500



if __name__ =="__main__":
    app.run(debug=True, port=5000)