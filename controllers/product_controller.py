from flask import Flask, render_template, request, redirect, Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_blueprint = Blueprint("products", __name__)

@product_blueprint.route('/products') #This displays product index
def products():
    products = product_repository.select_all_products()
    suppliers = supplier_repository.select_all_suppliers()
    return render_template("/products/index.html", products = products, suppliers = suppliers)

@product_blueprint.route('/products/new', methods = ['GET']) #This goes to a new product page
def new_product():
    suppliers = supplier_repository.select_all_suppliers()
    return render_template("products/new.html", suppliers = suppliers)

@product_blueprint.route('/products', methods=['POST']) #This creates new product from entered information and redirects to product page
def create_product():
    name = request.form['name']
    description = request.form['description']
    buying_cost = request.form['buying_cost']
    sell_price = request.form['sell_price']
    stock_count = request.form['stock_count']
    type_of_product = request.form['type_of_product']
    supplier_id = request.form['supplier_id']
    supplier=supplier_repository.select_supplier(supplier_id)
    product=Product(name, description, buying_cost, sell_price, stock_count, type_of_product, supplier, id)
    product_repository.save_product(product)
    return redirect('/products')

@product_blueprint.route('/products/<id>', methods=["GET"]) #This shows a single product
def show_product(id):
    product = product_repository.select_product(id)
    return render_template('products/show.html', product = product)

@product_blueprint.route('/products/<id>/edit', methods=['GET']) #This goes to an edit page for a product
def edit_product(id):
    product = product_repository.select_product(id)
    suppliers = supplier_repository.select_all_suppliers()
    return render_template('/products/edit.html', product=product, suppliers=suppliers)

@product_blueprint.route('/products/<id>', methods=['POST']) #This updates an edited product with entered information and goes to product page
def update_product(id):
    name = request.form['name']
    description = request.form['description']
    buying_cost = request.form['buying_cost']
    sell_price = request.form['sell_price']
    stock_count = request.form['stock_count']
    type_of_product = request.form['type_of_product']
    supplier_id = request.form['supplier_id']
    supplier=supplier_repository.select_supplier(supplier_id)
    product=Product(name, description, buying_cost, sell_price, stock_count, type_of_product, supplier, id)
    product_repository.update_product(product)
    return redirect('/products')

@product_blueprint.route('/products/via/<id>', methods=["GET"]) #This filters products based on entered information
def product_via_supplier(id):
    id=id
    products = product_repository.select_all_products()
    return render_template("/products/filters.html", products = products, id=id)