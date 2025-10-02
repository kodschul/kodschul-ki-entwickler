from mysql.connector import Error

import mysql.connector


def funcFetchUserById(userId, dbConfig):
    """
    Fetch a user from MySQL database by user ID.

    Args:
        userId (int): The ID of the user to fetch.
        dbConfig (dict): Dictionary with MySQL connection parameters.

    Returns:
        dict or None: User data as a dictionary if found, else None.
    """
    if not isinstance(userId, int) or userId <= 0:
        raise ValueError("userId must be a positive integer.")

    try:
        connection = mysql.connector.connect(
            host=dbConfig.get('host'),
            user=dbConfig.get('user'),
            password=dbConfig.get('password'),
            database=dbConfig.get('database'),
            port=dbConfig.get('port', 3306)
        )
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (userId,))
        user = cursor.fetchone()
        return user
    except Error as err:
        # Log error securely in production
        print("Database error occurred.")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
