import requests
import json


from flask import Flask, render_template



MENU_TEXT = """

Choose the following options:

[1] : Convert text one time.
[2] : Convert text in a continous stream.
[3] : Check the last saved entry.

[0] : Exit.
\n> """


class Communicator(object):

    def __init__(self):
        pass

    def send_recieve(self, to_send):
        post_request = requests.post(
            "http://127.0.0.1:5000/ask/", json=to_send)

        # fetch post-response as json and print to terminal
        response = post_request.json()
        print(response["processed_entry"])

    def read_last(self):
        post_request = requests.get("http://127.0.0.1:5000/last/")

        # fetch post-response as json and print to terminal
        response = post_request.json()
        original_entry = response["entry_string"]
        processed_entry = response["processed_entry"]
        print(f"{original_entry} -> {processed_entry}")


#def main():
#    options = input(MENU_TEXT)
#    c = Communicator()
#
#    if options == "1":
#        to_send = input("Type what you want to send\n> ")
#
#        # turn input into dict to pass through request.post() as json
#        # conversion between dict and json is automatic 
#        to_send  = {"entry_string": to_send}
#        c.send_recieve(to_send)
#    elif options == "2":
#        print("Type what you want to send. \nType 'q' to quit.")
#
#        while True:
#            to_send = input("\n> ")
#
#            if to_send == "q":
#                quit()
#
#            # turn input into dict to pass through request.post() as json
#            # conversion between dict and json is automatic
#            to_send  = {"entry_string": to_send}
#            c.send_recieve(to_send)
#    elif options == "3":
#        c.read_last()
#    elif options == "0":
#        quit()
#    else:
#        print("Option not recognised. Try again.")
#        main()


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


#if __name__ == "__main__":
    #main()

