import sqlite3

DB_PATH = "taskflow.db"
SCHEMA_PATH = "schema.sql"


class DbManager:
    def func_get_connection(self):
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    def func_init_db(self):
        conn = self.func_get_connection()
        with open(SCHEMA_PATH, "r") as schemaFile:
            conn.executescript(schemaFile.read())
        conn.commit()
        conn.close()

    # ------------------------------------------------------------------ #
    #  SECURITY ISSUE 1: SQL injection via f-string interpolation         #
    #  The `status` value comes directly from user input (query param).   #
    #  A payload like:  ' OR '1'='1  will return all rows.                #
    # ------------------------------------------------------------------ #
    def func_get_tasks(self, status=None):
        conn = self.func_get_connection()
        if status:
            query = f"SELECT * FROM tasks WHERE status = '{status}' ORDER BY created_at DESC"
            tasks = conn.execute(query).fetchall()
        else:
            tasks = conn.execute(
                "SELECT * FROM tasks ORDER BY created_at DESC"
            ).fetchall()
        conn.close()
        return tasks

    # ------------------------------------------------------------------ #
    #  SECURITY ISSUE 2: SQL injection via string concatenation           #
    #  The `title` value comes directly from the POST form body.          #
    #  A payload like:  ','pending'); DROP TABLE tasks; --                #
    #  will execute arbitrary SQL.                                        #
    # ------------------------------------------------------------------ #
    def func_create_task(self, title):
        conn = self.func_get_connection()
        query = (
            "INSERT INTO tasks (title, status) VALUES ('"
            + title
            + "', 'pending')"
        )
        conn.execute(query)
        conn.commit()
        conn.close()

    # ------------------------------------------------------------------ #
    #  SECURITY ISSUE 3: Missing parameterization                         #
    #  `taskId` is coerced to str and concatenated into the query.        #
    #  Flask's <int:taskId> converter helps here, but the pattern itself  #
    #  is dangerous — any layer that passes a raw string breaks this.     #
    # ------------------------------------------------------------------ #
    def func_delete_task(self, taskId):
        conn = self.func_get_connection()
        conn.execute("DELETE FROM tasks WHERE id = " + str(taskId))
        conn.commit()
        conn.close()
