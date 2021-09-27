from db.run_sql import run_sql
from models.product import Product
import repositories.supplier_repository as supplier_repository 

def save_product(product):
    sql = "INSERT INTO products (name, description, buying_cost, sell_price, stock_count, type_of_product, supplier_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.buying_cost, product.sell_price, product.stock_count, product.type_of_product, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all_products():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for result in results:
        supplier = supplier_repository.select_supplier(result['supplier_id'])
        product = Product(result['name'], result['description'], result['buying_cost'], result['sell_price'], result['stock_count'], result['type_of_product'], supplier, result['id'])
        products.append(product)
    return products

def select_product(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = supplier_repository.select_supplier(result['supplier_id'])
        product = Product(result['name'], result['description'], result['buying_cost'], result['sell_price'], result['stock_count'], result['type_of_product'], supplier, result['id'])
    return product

def delete_all_products():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete_product(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update_product(product):
    sql = "UPDATE products SET (name, description, buying_cost, sell_price, stock_count, type_of_product, supplier_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.buying_cost, product.sell_price, product.stock_count, product.type_of_product, product.supplier.id]
    run_sql(sql, values)

