from db.run_sql import run_sql
from models.product import Product
from models.supplier import Supplier



def save_product(product):
    sql = "INSERT INTO products (name, description, buying_cost, sell_price, stock_count, type_of_product, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.buying_cost, product.sell_price, product.stock_count, product.type_of_product, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product
