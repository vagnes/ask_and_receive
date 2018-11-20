import requests
import json


class Communicator(object):

    @staticmethod
    def send_recieve(to_send):
        post_request = requests.post(
            "http://127.0.0.1:5000/ask/", json=to_send)

        # fetch post-response as json and print to terminal
        response = post_request.json()
        return response["processed_entry"]

    @staticmethod
    def read_last():
        post_request = requests.get("http://127.0.0.1:5000/last/")

        # fetch post-response as json and print to terminal
        response = post_request.json()
        original_entry = response["entry_string"]
        processed_entry = response["processed_entry"]
        print(f"{original_entry} -> {processed_entry}")

