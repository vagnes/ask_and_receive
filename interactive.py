import requests

MENU_TEXT = """

Choose the following options:

[1] : Convert text one time.
[2] : Convert text in a continous stream.
[3] : Check the last saved text.

[0] : Exit.
\n> """


class Communicator(object):

    def __init__(self):
        pass

    def send_recieve(self, to_send):
        post_request = requests.post(
            "http://127.0.0.1:5000/ask/", data=to_send)
        print(post_request.content.decode("utf-8"))

    def read_last(self):
        post_request = requests.get("http://127.0.0.1:5000/last/")
        print(post_request.content.decode("utf-8"))


def main():
    options = input(MENU_TEXT)
    c = Communicator()

    if options == "1":
        to_send = input("Type what you want to send\n> ")
        c.send_recieve(to_send)
    elif options == "2":
        print("Type what you want to send. \nType 'q' to quit.")
        while True:
            to_send = input("\n> ")
            if to_send == "q":
                quit()
            c.send_recieve(to_send)
    elif options == "3":
        c.read_last()
    elif options == "0":
        quit()
    else:
        print("Option not recognised. Try again.")
        main()


if __name__ == "__main__":
    main()
