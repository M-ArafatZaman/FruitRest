from data.DB import DB
import sqlite3

"""
The database layer is where all the database related logic resides.

The database layer is responsible for:
- Connecting to the database
- Executing raw SQL queries on the database
- Error handling for database operations

Here the service layer passes the database related operations to the database layer.

Other layers like the service layer who use the database layer do not care about how the database layer works,
they only care about the results of the database operations.

The database layer can be modified to use whatever database we want,
like MySQL, PostgreSQL, MongoDB, etc. as long as the interface remains the same.
The service layer does not need to be modified if we change the database.
"""

class HelloDB(DB):
    def connect(self):
        # Using a in-memory database for this example
        # An in-memory database is created when the connection is opened
        # and destroyed when the connection is closed. Making it a temporary
        # database that only exists in the memory of the application
        self.connection = sqlite3.connect("hello.db")
        self.app.logger.info("Connected to in-memory database")

    def getHelloMessageFromDB(self):
        self.app.logger.info("Fetching hello message from database")
        cursor = self.connection.cursor()

        try:
            cursor.execute("SELECT messageText FROM helloTable WHERE messageName = 'hello';")
            message = cursor.fetchone()[0]
        except sqlite3.Error as e:
            self.app.logger.error(f"Error fetching message: {e}")
            return

        cursor.close()
        return message

    def createHelloTable(self):
        self.app.logger.info("Creating hello table in database")
        cursor = self.connection.cursor()

        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS helloTable (messageName TEXT, messageText TEXT);")
            self.connection.commit()
        except sqlite3.Error as e:
            self.app.logger.error(f"Error creating table: {e}")
            return

        cursor.close()
        self.app.logger.info("Hello table created in database")

    def insertHelloMessage(self, message):
        self.app.logger.info("Inserting hello message into database")
        cursor = self.connection.cursor()

        try:
            cursor.execute("INSERT INTO helloTable (messageName, messageText) VALUES ('hello', ?);", (message,))
            self.connection.commit()
        except sqlite3.Error as e:
            self.app.logger.error(f"Error inserting message: {e}")
            return

        cursor.close()
        self.app.logger.info("Hello message inserted into database")