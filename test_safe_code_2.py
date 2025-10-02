from mysql.connector import Error

import mysql.connector


class UserDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def funcConnect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                return True
            return False
        except Error as err:
            # Log error securely, do not expose sensitive info
            print("Database connection error.")
            return False

    def funcFetchUser(self, userId):
        if not isinstance(userId, int):
            raise ValueError("Invalid userId type.")
        if self.connection is None or not self.connection.is_connected():
            raise ConnectionError("Not connected to the database.")
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT id, username, email FROM users WHERE id = %s"
            cursor.execute(query, (userId,))
            user = cursor.fetchone()
            cursor.close()
            return user
        except Error as err:
            # Log error securely, do not expose sensitive info
            print("Error fetching user.")
            return None

    def funcCloseConnection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
