from flask import Flask, request

from flask_restful import Resource, Api

import requests
import json


app = Flask(__name__)
api = Api(app)


# Constants
JSON_FILE = 'saved_entries.json'


def send_to_processor(to_send):
    print(f"Sent '{to_send}' to processor.")
    requests.post("http://127.0.0.1:5001/processor/", json=to_send)


def update_json_file(to_save):
    """ stores json-string in JSON_FILE using python.json() """
    with open(file=JSON_FILE, mode="w") as jason:
        json.dump(to_save, jason)


def load_json_file():
    """ returns JSON_FILEs' content as python.dict() """
    with open(file=JSON_FILE, mode="r") as jason:
        file_content = json.load(jason)
        return file_content


class Index(Resource):

    def get(self):
        return "IT WIRKLS"


class Ask(Resource):

    def post(self):
        print("\n--Connection init--")

        # request.get_json retursn the json-obj as a python-dict()
        to_send = request.get_json()
        send_to_processor(to_send)
        to_return = load_json_file()
        return to_return


class Recieve(Resource):

    def post(self):
        # extract entry from json before saving to file
        to_save = request.get_json()
        print(to_save)
        update_json_file(to_save)

class Last(Resource):

    def get(self):
        return load_json_file()


api.add_resource(Index, "/")
api.add_resource(Ask, "/ask/")
api.add_resource(Recieve, "/recieve/")
api.add_resource(Last, "/last/")


if __name__ == "__main__":
    app.run(port=5000, threaded=True, debug=True)
