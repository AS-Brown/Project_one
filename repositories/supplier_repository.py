from db.run_sql import run_sql
from models.supplier import Supplier

def save_supplier(supplier): #This saves a supplier
    sql = "INSERT INTO suppliers (name, location, active) VALUES (%s, %s, %s) RETURNING *"
    values = [supplier.name, supplier.location, supplier.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier

def select_all_suppliers(): #This selects all suppliers
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for result in results:
        supplier = Supplier(result['name'], result['location'], result['active'], result['id'] )
        suppliers.append(supplier)
    return suppliers

def select_supplier(id): #This selects a supplier via their id
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = Supplier(result['name'], result['location'], result['active'], result['id'] )
    return supplier

def update_supplier(supplier): #This updates a supplier
    sql = "UPDATE suppliers SET (name, location, active) = (%s, %s, %s) WHERE id = %s"
    values = [supplier.name, supplier.location,supplier.active, supplier.id]
    run_sql(sql, values)    

def delete_all_suppliers(): #This deletes all suppliers
    sql = "DELETE FROM suppliers"
    run_sql(sql)

def delete_supplier(id): #This deletes a supplier via their id
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

