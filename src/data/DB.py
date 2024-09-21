# 2024 (c) Mohammad Arafat Zaman

"""
A database class in a web application is responsible for
connecting to the database and executing queries. It acts
as a bridge between the service layer and the database.

We are using an abstract class to define the database class
so that all database classes must implement the connect method.
"""

from abc import abstractmethod
from flask import Flask

class DB:
    def __init__(self, app: Flask):
        self.app: Flask = app

    @abstractmethod
    def connect(self):
        pass