from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)


def send_to_processor(to_send):
    print(f"Sent '{to_send}' to processor.")
    requests.post("http://127.0.0.1:5001/processor/", data=to_send)


def save_to_txt(to_save):
    with open(file="saved_text.txt", mode="w") as f:
        f.write(str(to_save))


def load_from_txt():
    with open(file="saved_text.txt", mode="r") as f:
        return f.read()


class Index(Resource):

    def get(self):
        return "IT WIRKLS"


class Ask(Resource):

    def post(self):
        print("\n--Connection init--")
        to_send = request.get_data().decode("utf-8")
        print(to_send)
        send_to_processor(to_send)
        to_return = load_from_txt()
        return to_return


class Recieve(Resource):

    def post(self):
        to_save = request.get_data()
        to_save = to_save.decode("utf-8")
        print(to_save)
        save_to_txt(to_save)


api.add_resource(Index, "/")
api.add_resource(Ask, "/ask/")
api.add_resource(Recieve, "/recieve/")

if __name__ == "__main__":
    app.run(port=5000, threaded=True, debug=True)
