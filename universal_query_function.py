from db_connect import *

def return_query_results(conn, query):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute(query)
        while True:
            row = query.fetchone()
            if row is None:
                break
            print(row)


# connection = db_connect_me()
# query = "SELECT * FROM Orders o WHERE o.ShipCity IN ('Rio De Janeiro', 'Reims')"
# return_query_results(connection, query)
