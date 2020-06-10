from db_connect import *


def question_one(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute('SELECT COUNT(o.OrderID) FROM Orders o;')
        print(query.fetchone()[0])


def question_two(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute("SELECT COUNT(o.OrderID) FROM Orders o WHERE o.ShipCity = 'Rio De Janeiro';")
        print(query.fetchone()[0])


def question_three(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute("SELECT * FROM Orders o WHERE o.ShipCity IN ('Rio De Janeiro', 'Reims')")
        while True:
            row = query.fetchone()
            if row is None:
                break
            print(row)


def question_four(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute("SELECT * FROM Customers c WHERE c.CompanyName LIKE ('%Z%')")
        while True:
            row = query.fetchone()
            if row is None:
                break
            print(row)


def question_five(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute("SELECT c.CustomerID, c.CompanyName, c.ContactName, c.Phone, c.Fax FROM Customers c WHERE c.Fax IS NULL ")
        while True:
            row = query.fetchone()
            if row is None:
                break
            print(row)


def question_six(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute("SELECT * FROM Customers c WHERE c.City = 'Paris'")
        while True:
            row = query.fetchone()
            if row is None:
                break
            print(row)


def question_seven(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute("SELECT TOP 5 c.CustomerID, c.ContactName, SUM(od.Quantity) FROM Customers c INNER JOIN Orders o ON c.CustomerID = o.CustomerID INNER JOIN [Order Details] od ON o.OrderID = od.OrderID WHERE c.City = 'Paris' GROUP BY c.CustomerID, c.ContactName ORDER BY SUM(od.Quantity)")
        while True:
            row = query.fetchone()
            if row is None:
                break
            print(row)


def question_eight(conn):
    with conn:
        cursor = conn.cursor()
        query = cursor.execute("SELECT TOP 5 c.CustomerID, c.ContactName, c.CompanyName, c.Phone, c.Address, SUM(od.TQuan), COUNT(od.OrderID) FROM Customers c INNER JOIN Orders o ON c.CustomerID = o.CustomerID INNER JOIN (SELECT DISTINCT OrderID, SUM(Quantity) AS TQuan FROM [Order Details] GROUP BY OrderID) od ON od.OrderID = o.OrderID WHERE c.City = 'Paris' AND DATEDIFF(dd, o.OrderDate, o.ShippedDate) > 0 GROUP BY c.CustomerID, c.ContactName, c.CompanyName, c.Phone, c.Address ORDER BY SUM(od.TQuan)")
        while True:
            row = query.fetchone()
            if row is None:
                break
            print(row)


connection = db_connect_me()
# question_one(connection)
# question_two(connection)
# question_three(connection)
# question_four(connection)
# question_five(connection)
# question_six(connection)
# question_seven(connection)
# question_eight(connection)
