from flask import Flask, render_template, request, redirect, Blueprint
from models.product import Product
import repositories.product_repository as product_repository

product_blueprint = Blueprint("products", __name__)

@product_blueprint.route('/products')
def products():
    products = product_repository.select_all_products()
    return render_template("/products/index.html", products = products)