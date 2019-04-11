from server import app, api
from flask import request
from flask_restful import Resource
import requests
from random import randrange


def ask_processing(to_process):
    """ changes capitalization of letters at random """
    to_output = ""

    for letter in to_process:
        if randrange(0, 2) is 1:
            to_output += letter.capitalize()
        else:
            to_output += letter

    return to_output


class GetQuote(Resource):

    def post(self):
        user_input = request.get_json()
        response = ask_processing(user_input["user_input"])
        return response


api.add_resource(GetQuote, "/getquote/")

if __name__ == "__main__":
    app.run(port=5001, debug=True)
