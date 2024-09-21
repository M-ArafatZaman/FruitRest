from controller.Controller import Controller
from service.HelloService import HelloService

"""
The controller receives the request from the router
and passes it to the service for processing.
It returns whatever the service returns.

Any logic specific to the request proxy, 
should be handled here.

For example,
- Checking if any necessary headers/cookies are present
- Checking if the user/request is authenticated
- Checking if the request is valid, not a spam
- Checking if the user has the right permissions
- Modifying the request before passing it to the service
- Logging the request (Keeping track of it in the database or a log file)

The controller does not care about the business logic,
it only cares about routing the request to the right service.
"""

class HelloController(Controller):
    def call(self):
        self.app.logger.info("HelloController called, passing request to HelloService")
        return HelloService(self.app).process()