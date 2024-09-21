from service.Service import Service
from api.helloApi import FetchHelloMessage
from data.helloDB import HelloDB
from flask import jsonify

"""
The service is where the business logic of the application resides.
It is kind of like the brain of the application.

Here the controller passes the request to the service for processing.

The service here performs all the business logic.

For example, in this case, the service:
- Connects to the database
- Checks if the hello message exists in the database
- If it does not exist, fetches the message from the API
- Inserts the message into the database
- Returns the message to the controller

The service layer does not care about the routing or the request,
It also makes use of other layer components like the database layer and the API layer.
It does not care how the API layer and the database layer work, it only cares about
implementing the core business logic.
"""

class HelloService(Service):
    def process(self):
        db = HelloDB(self.app)
        db.connect()

        helloMessage = db.getHelloMessageFromDB()

        if not helloMessage:
            """
            If the message does not exist in the database, create it
            """
            self.app.logger.info("Hello message not found in database, creating message")
            db.createHelloTable()
            helloMessage = FetchHelloMessage(self.app).get()["message"]
            db.insertHelloMessage(helloMessage)

        return jsonify({
            "message": helloMessage
        })