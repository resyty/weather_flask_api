from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Meteo API',
    description='abellenoue',
)

ns = api.namespace('meteo', description='meteo stations')

station = api.model('Stations', {
    'id_station': fields.String(required=True, description='identifiant de la station'),
    'id_sonde': fields.String(required=True, description='identifiant de la sonde'),
    'latitude': fields.Float(required=True),
    'longitude': fields.Float(required=True),
    'ville':fields.String(required=True),
    'timestamp':fields.Integer(required=True),
    'temperature':fields.Float(required=True),
    'humidite':fields.Float(required=True)  
})

class stationDAO(object):
    def __init__(self):
        super().__init__()
    def create(self,data):
        station=data
        return station

DAO=stationDAO()

@ns.route('/')
class TodoList(Resource):
    @ns.doc('create_station')
    @ns.expect(station)
    @ns.marshal_with(station, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


if __name__ == '__main__':
    app.run(debug=True)