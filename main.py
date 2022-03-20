from flask import flask
from flask_restful import Api, Resource, reqparse
import random

api = Flask(__name__)
api = Api(app)

info = [
	{
		"id": 0,
		"balance": 0	
	},
	{
		"id": 1,
		"balance": 1
	},
	{
		"id": 2,
		"balance": 2
	}
]

print(info)

class Quote(Resource):
	def get(self, id=0):
		if id == 0:
			return random.choice(info), 200
		for quote in info:
			if(quote['id'] == id):
				return quote, 200
		return "Информация не найдена!", 404

	def post(self, id):
		parser = reqparse.RequestParser()
		parser.add_argument("balance")
		params = parser.parse_args()
		for quote in info:
			if(id == quote['id']):
				return f"Информация с ID {id} уже существует!"
		quote = {
			"id": int(id),
			"balance": params['balance']
		}
		info.append(quote)
		return quote, 201

	def put(self, id):
		parser = reqparse.RequestParser()
		parser.add_argument("balance")
		params = parser.parse_args()
		for quote in info:
			if(id == quote['id']):
				quote['balance'] = params['balance']
				return quote, 200
		quote = {
			"id": int(id),
			"balance": params['balance']
		}

		info.append(quote)
		return quote, 201

	def delete(self, id):
		global info
		info = [quote for quote in info if quote['id'] != id]
		return f"Информация с ID {id} удалена!", 200

api.add_resource(Quote, "/info", "/info/", "/info/<int:id>")
if __name__ == "__main__":
	app.run(debug=True)
