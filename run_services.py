from sys import executable
from subprocess import Popen

Popen([executable, "ask_me.py"])
Popen([executable, "ask_processor.py"])
Popen([executable, "front_end.py"])

input("Press ENTER to exit.")