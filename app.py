from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)

CORS(app)

identitas = []

class ContohResource(Resource):
    def get(self):
        # response = {"msg": "Hello World"}
        response = {
            "msg": "success",
            "data": identitas
        }
        return response

    def post(self):
        nama = request.json['nama']
        umur = request.json['umur']
        identitas.append({
            "nama": nama,
            "umur": umur
        })
        response = {"msg": "Data berhasil dimasukan"}
        
        return response
api.add_resource(ContohResource, '/api', methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
