import pyodbc


def db_connect_me():
    server = 'databases2.spartaglobal.academy'
    database = 'Northwind'
    username = 'SA'
    password = 'Passw0rd2018'
    conn ='DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
    return pyodbc.connect(conn)

