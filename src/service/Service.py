# 2024 (c) Mohammad Arafat Zaman

"""
A service class in a web application is responsible for
processing the requests from the controller and returning
the response. It handles all the business logic of the
application.

We are using an abstract class to define the service class
so that all services must implement the process method.
"""

from abc import abstractmethod
from flask import Flask

class Service:
    def __init__(self, app: Flask):
        self.app: Flask = app
        
    @abstractmethod
    def process(self):
        pass