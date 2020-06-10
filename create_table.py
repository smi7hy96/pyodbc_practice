from db_connect import *
from universal_query_function import *


def create_database(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute("CREATE DATABASE ryan_db;")


def create_table(conn, table_query, db):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute(db, table_query)


def add_customer(conn, first_name, last_name):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute(f"""INSERT INTO Customer(
    first_name, last_name
)
VALUES
(
    {first_name}, {last_name}
);
""")


connection = db_connect_me()
creating_table_query = """CREATE TABLE Customer 
( 
customer_ID int NOT NULL IDENTITY(1,1) PRIMARY KEY, 
first_name VARCHAR(20), last_name VARCHAR(20));"""

database_use_code = "USE ryan_db;"


create_database(connection)
create_table(connection, creating_table_query, database_use_code)
f_name = input("Enter first name: \n")
l_name = input("Enter last name: \n")
add_customer(connection, f_name, l_name)
get_query = "SELECT * FROM Customer;"
return_query_results(connection, get_query)

