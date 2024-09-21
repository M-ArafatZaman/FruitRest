# 2024 (c) Mohammad Arafat Zaman


"""
A controller class in a web application is responsible for 
receiving requests from the client, and passing them to the
service layer.

We are using an abstract class to define the controller class
so that all controllers must implement the call method.
"""

from abc import abstractmethod
from flask import Flask

class Controller:
    def __init__(self, app: Flask):
        self.app: Flask = app

    @abstractmethod
    def call(self):
        pass

