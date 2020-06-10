# Connecting Python with DB

This class will allow our python to easily connect with our DB.

To do so, we will use a package called PYODBC.

This package abstracts our connections to the DB.

# PYODBC and OOP

We are looking into the PYODBC package.

And we are going to use the package to make a OOP module, that abstracts our interaction with the NW Database.

And then further abstract the interaction with specific Tables.

Finally, where appropriate we will use the CRUD design to build methods. 

## WHAT IS PYODBC

PYODBC is an OS module that makes accessing databases easy so that you can manipulate data using injected sql commands.

- Initialisation:
```python
product_instance = DBProduct()
```
- Now class is initialised, the methods within it can now be used (change name of product_instance to anything appropriate - it is just a variable)
## CRUD

CRUD is an acronym for four functions involved with data manipulation. Create, Read, Update, Delete
### CREATE - 
- Create (or INSERT) a row into the selected table. Make sure to order the Column names correctly.

```python
product_instance.insert_row(product_name, supplier_id,
 category_id, quantity_per_unit, unit_price, units_in_stock,
 units_on_order, reorder_level, discontinued))
```
- Replace each variable with a string/ int where appropriate. Or to create input statements to type in each variable name.

### READ -
- Read (or get) is when you retrieve the results of a SQL search query. You can get one result or every result using following examples.
#### - READ ONE
```python
print(product_instance.get_by_id(x))
```
- Where 'x' is an integer
#### - READ ALL
```python
print(product_instance.get_all())
```
- Retrieves every row from the products table
```python
print(product_instance.get_all(product_name))
```
- Retrieves every row from the products table that has the 'product_name' variable in the ProductName column
### UPDATE -
- Update is when you alter the values of a particular row
```python
print(product_instance.update_one_row(product_name, quantity_per_unit, product_id))
```
- Changes the ProductName and QuantityPerUnit at the row of the selected ProductID
### DELETE -
- Deletes a particular row
```python
print(product_instance.delete_one_row(product_id))
```
- Removes the row with the selected ProductID