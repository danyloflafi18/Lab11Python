from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from models.ua.lviv.iot.dangerLevel import DangerLevel
from models.ua.lviv.iot.insuranceType import InsuranceType

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI'] = \'mysql+mysqlconnector://root:0000@localhost:3306/insurance?auth_plugin=mysql_native_password'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Travel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))
    number_of_days = db.Column(db.Integer)
    telephone = db.Column(db.String(20))
    insurance_type = db.Column(db.String(15))
    medical_assistance = db.Column(db.String(15))
    accident = db.Column(db.String(15))

    def __init__(self,
                 name=None,
                 surname=None,
                 number_of_days=0,
                 telephone=None,
                 insurance_type=InsuranceType.HEALTH,
                 medical_assistance=DangerLevel.HIGH,
                 accident=DangerLevel.LOW
                 ):
        self.name = name
        self.surname = surname
        self.number_of_days = number_of_days
        self.telephone = telephone
        self.insurance_type = insurance_type
        self.medical_assistance = medical_assistance
        self.accident = accident


class TravelSchema(ma.Schema):
    class Meta:
        fields = (
            'name', 'surname', 'number_of_days',
            'telephone', 'insurance_type',
            'medical_assistance', 'accident'
        )


travel_schema = TravelSchema()
travels_schema = TravelSchema(many=True)


# endpoint to create new travel
@app.route("/travel", methods=["POST"])
def add_travel():
    name = request.json['name']
    surname = request.json['surname']
    number_of_days = request.json['number_of_days']
    telephone = request.json['telephone']
    insurance_type = request.json['insurance_type']
    medical_assistance = request.json['medical_assistance']
    accident = request.json['accident']

    new_travel = Travel(
        name, surname, number_of_days,
        telephone, insurance_type,
        medical_assistance, accident
        )

    db.session.add(new_travel)
    db.session.commit()

    return jsonify(request.json)


# endpoint to show all travels
@app.route("/travel", methods=["GET"])
def get_travel():
    all_travels = Travel.query.all()
    result = travels_schema.dump(all_travels)
    return jsonify(result.data)


# endpoint to get travel detail by id
@app.route("/travel/<id>", methods=["GET"])
def travel_detail(id):
    travel = Travel.query.get(id)
    return travel_schema.jsonify(travel)


# endpoint to update travel
@app.route("/travel/<id>", methods=["PUT"])
def travel_update(id):
    travel = Travel.query.get(id)
    travel.name = request.json['name']
    travel.surname = request.json['surname']
    travel.number_of_days = request.json['number_of_days']
    travel.telephone = request.json['telephone']
    travel.insurance_type = request.json['insurance_type']
    travel.medical_assistance = request.json['medical_assistance']
    travel.accident = request.json['accident']

    db.session.commit()
    return travel_schema.jsonify(travel)


# endpoint to delete travel
@app.route("/travel/<id>", methods=["DELETE"])
def travel_delete(id):
    travel = Travel.query.get(id)
    db.session.delete(travel)
    db.session.commit()

    return travel_schema.jsonify(travel)


if __name__ == '__main__':
    app.run(debug=True)