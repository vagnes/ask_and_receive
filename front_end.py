import requests
import json


from flask import Flask, render_template, request


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


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    output = None
    if request.method == "POST":
        entry = request.form["aar_input"]
        entry = {"entry_string": entry}
        output = Communicator.send_recieve(entry)
        return render_template("index.html", output=output)
    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(port=5003)
