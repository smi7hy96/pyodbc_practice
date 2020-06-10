from oop_files.db_products import DBProduct
from oop_files.db_customer import DBCustomers

product_table = DBProduct()
customer_table = DBCustomers()
print(product_table.get_by_id(1))
print(product_table.get_all())
print(product_table.get_all('Anton'))
print(customer_table.get_by_id('AROUT'))
print(customer_table.get_all())
print(customer_table.get_all('Maria'))
