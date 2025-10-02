

import mysql.connector

dbHost = "localhost"
dbUser = "root"
dbPassword = "your_password"
dbDatabase = "your_database"
dbConnection = mysql.connector.connect(
    host=dbHost,
    user=dbUser,
    password=dbPassword,
    database=dbDatabase
)


def funcFetchUserByUsername(dbConnection, userName):
    cursor = dbConnection.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (userName,))
    result = cursor.fetchone()
    cursor.close()
    return result
