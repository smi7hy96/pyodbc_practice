from oop_files.db_products import DBProduct


product_table = DBProduct()

print(product_table.get_by_id(1))
print(product_table.get_all())
print(product_table.get_all('Anton'))
