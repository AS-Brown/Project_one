from db.run_sql import run_sql
from models.supplier import Supplier

def save_supplier(supplier):
    sql = "INSERT INTO suppliers (name) VALUES (%s) RETURNING *"
    values = [supplier.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier

def select_all_suppliers():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for result in results:
        supplier = Supplier(result['name'], result['id'] )
        suppliers.append(supplier)
    return suppliers

def select_supplier(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = Supplier(result['name'], result['id'] )
    return supplier

def delete_all_suppliers():
    sql = "DELETE FROM suppliers"
    run_sql(sql)

def delete_supplier(id):
    sql = "DELETE FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)