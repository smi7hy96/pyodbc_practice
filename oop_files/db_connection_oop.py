import pyodbc

class MSDBConnection:
    def __init__(self, database="Northwind", server='databases2.spartaglobal.academy', username='SA', password='Passw0rd2018'):        # Establish connection with any db in MSsql
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        # Making ocnnection & Cursor
        self.conn = self._establish_connection()
        self.cursor = self.conn.cursor()

    def _establish_connection(self):
        conn = 'DRIVER={SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password
        return pyodbc.connect(conn)

    # open to sql injections - use a separate method to validate string first
    def __sql_query_execute(self, sql_string):
        return self.cursor.execute(sql_string)

    def sql_query(self, sql_string):
        # Filter and Validate First Here
        return self.__sql_query_execute(sql_string)