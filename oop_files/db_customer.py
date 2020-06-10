from oop_files.db_connection_oop import MSDBConnection


class DBCustomers(MSDBConnection):

    def __init__(self):
        super().__init__()

    def get_by_id(self, id):
        return self.sql_query(f"SELECT * FROM Customers WHERE CustomerID = '{id}'").fetchone()

    def get_all(self, customer_name=None):
        result_list = []
        if customer_name is None:
            q_result = self.sql_query('SELECT * FROM Customers')
        else:
            q_result = self.sql_query(f"SELECT * FROM Customers WHERE ContactName LIKE ('%{customer_name}%')")
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list

# Create one method
    def insert_row(self, company_name, contact_name, contact_title, address, city, region, postal_code, country, phone, fax):
        self.sql_query(f"""INSERT INTO Customers
(
CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax
)
VALUES
(
'{company_name}', '{contact_name}', '{contact_title}', '{address}', '{city}', '{region}', '{postal_code}', '{country}', '{phone}', '{fax}
);
""")
        self.conn.commit()

# update one method (similar to get by id)
    def update_one_row(self, customer_name, city, phone, customer_id):
        self.sql_query(f"""UPDATE Customers
SET ContactName = '{customer_name}', City = '{city}', Phone = '{phone}'
WHERE CustomerID = {customer_id}""")
        self.conn.commit()

# delete one method ( CAREFULLY ) by id
    def delete_one_row(self, customer_id):
        self.sql_query(f"""DELETE FROM Customers WHERE CustomerID = {customer_id}""")
        self.conn.commit()
