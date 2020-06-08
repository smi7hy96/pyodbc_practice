import pyodbc


# DB Connection Variables
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
conn ='DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

# Establish Connection
connection = pyodbc.connect(conn)


# Making a cursor (This keeps state)
cursor = connection.cursor()

# quick print check

print(connection)
print(cursor)

# Perform Query

query_result = cursor.execute('SELECT * FROM Products')
print(query_result.fetchone())  # get first row - cursor keeps state so second use of fetchone now gets second row
# -fetchall()- retrieves whole table from query, cursor at end ie. stack empty
# to get back to first row, new cursor needed (or execute again)

data_point = query_result.fetchone()
# Behaves like an iterable list - organised with index
print(data_point[1])
# Also behave like an OOP Object, where the initialised parameters are the column names
print(data_point.ProductName)

# iterating through everything with fetchone()
while True:
    row = query_result.fetchone()
    if row is None:
        break
    print(row)

# for row in query_result.fetchall():  # returns a list - iterate through list - display all rows
#     print(row.ProductName, row.UnitPrice, row.QuantityPerUnit)  # Selected certain comments
