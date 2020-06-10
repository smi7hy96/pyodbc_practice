from oop_files.db_connection_oop import MSDBConnection


class DBProduct(MSDBConnection):

    def __init__(self):
        super().__init__()

    def get_by_id(self, id):
        return self.sql_query(f'SELECT * FROM Products WHERE ProductID = {int(id)}').fetchone()


    def get_all(self, product_name = None):
        result_list = []
        if product_name is None:
            q_result = self.sql_query('SELECT * FROM Products')
        else:
            q_result = self.sql_query(f"SELECT * FROM Products WHERE ProductName LIKE ('%{product_name}%')")
        while True:
            row = q_result.fetchone()
            if row is None:
                break
            result_list.append(row)
        return result_list


# Create one method

# update one method (similar to get by id)

# delete one method ( CAREFULLY ) by id