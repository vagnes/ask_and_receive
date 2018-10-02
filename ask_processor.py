from flask import Flask, request
from flask_restful import Resource, Api
from time import sleep
import requests
from random import randrange

app = Flask(__name__)
api = Api(app)

def send_to_ask(to_send):
	print(f"Sent {to_send} to ask.")
	requests.post("http://127.0.0.1:5000/recieve/", data=to_send)


def ask_processing(to_process):
	to_output = ""

	for letter in to_process:
		if randrange(0, 2) is 1:
			to_output += letter.capitalize()
		else:
			to_output += letter

	return to_output


class Index(Resource):

	def get(self):
		return "IT WIRKLS"


class Processor(Resource):

	def post(self):
		to_send = request.get_data().decode("utf-8")
		sleep(0.1)
		send_to_ask(ask_processing(to_send))


api.add_resource(Index, "/")
api.add_resource(Processor, "/processor/")

if __name__ == "__main__":
	app.run(port=5001, threaded=True, debug=True)
