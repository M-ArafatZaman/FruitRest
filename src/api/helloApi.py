from api.APIBase import APIBase
import requests

"""
The API layer is where all the API calls are made.

The service layer uses the API layer to fetch data from external APIs.

The API layer is responsible for:
- Making API calls
- Error handling for API calls
- Parsing the API response
- Returning the API response to the service layer

The service layer does not care about how the API layer works,
it only cares about the results of the API calls.

We can use other libraries instead of the `requests` library to make API calls,
The service layer will not need to be modified if we change the API library.
"""

class FetchHelloMessage(APIBase):
    endpoint = "https://postman-echo.com/get?message=Hello%20world!"

    def get(self):
        return requests.get(self.endpoint).json()["args"]