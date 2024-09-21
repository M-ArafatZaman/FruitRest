from flask import Flask, request
from constants import METHODS
from controller.HelloController import HelloController

app = Flask(__name__)

"""
Example endpoint
localhost:5000/ will execute this hello function.
We re-route it to a controller to keep the controlling logic seperate from
the app/routing logic.

The router does not care about the business logic, it only cares about
routing the request to the right controller.
"""
@app.route('/', methods=[METHODS.GET])
def hello():
    app.logger.info(f"Request received: {request}")
    return HelloController(app).call()

