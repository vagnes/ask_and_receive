# Ask and recieve

A very simple example of how microservices can be tied together with a RESTful API in Flask.

To run, launch both of the Python services and run *front_end.py* to communicate with the services through a front-end interface. You can also curl from the terminal, or simply use the *rest_cli.py* program.

```text
curl 127.0.0.1:5000/ask/ -d "This is a test."
```

TODO
* Implement HTTPS