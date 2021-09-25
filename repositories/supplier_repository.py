from db.run_sql import run_sql
from models.supplier import Supplier
from models.product import Product

def save_supplier(supplier):
    sql = "INSERT INTO suppliers (name) VALUES (%s) RETURNING *"
    values = [supplier.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier


