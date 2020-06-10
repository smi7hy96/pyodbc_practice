from oop_files.db_connection_oop import MSDBConnection


class DBProduct(MSDBConnection):

    def __init__(self):
        super().__init__()

    def get_by_id(self, id):
        return self.sql_query(f'SELECT * FROM Products WHERE ProductID = {int(id)}').fetchone()

    def get_all(self, product_name=None):
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
    def insert_row(self, product_name, supplier_id, category_id, quantity_per_unit, unit_price, units_in_stock, units_on_order, reorder_level, discontinued):
        self.sql_query(f"""INSERT INTO Products
(
ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued
)
VALUES
(
'{product_name}', {supplier_id}, {category_id}, '{quantity_per_unit}', {unit_price}, {units_in_stock}, {units_on_order}, {reorder_level}, {discontinued}
);
""")

# update one method (similar to get by id)
    def update_one_row(self, product_name, quantity_per_unit, product_id):
        self.sql_query(f"""UPDATE Products
SET ProductName = '{product_name}', QuantityPerUnit = '{quantity_per_unit}'
WHERE ProductID = {int(product_id)}""")

# delete one method ( CAREFULLY ) by id
    def delete_one_row(self, product_id):
        self.sql_query(f"""DELETE FROM Products WHERE ProductID = {product_id}""")
