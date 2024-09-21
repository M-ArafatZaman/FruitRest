# 2024 (c) Mohammad Arafat Zaman

"""
The API layer is responsible for making all the API calls to 
other services or external APIs. It acts as a bridge between
the service layer and the external world.

We are using an abstract class to define the API class so that
all APIs must implement the get or post method.
"""

from abc import abstractmethod
from flask import Flask

class APIBase:
    def __init__(self, app: Flask):
        self.app: Flask = app

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass