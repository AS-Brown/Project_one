from flask import Flask, render_template, request, redirect, Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

supplier_blueprint = Blueprint("suppliers", __name__)

@supplier_blueprint.route('/suppliers')
def suppliers():
    suppliers = supplier_repository.select_all_suppliers()
    return render_template("/suppliers/index.html", suppliers = suppliers)

@supplier_blueprint.route('/suppliers/new')
def new_supplier():
    return render_template('/suppliers/new.html')

@supplier_blueprint.route('/suppliers', methods=['POST'])
def create_supplier():
    name = request.form['name']
    location = request.form['location']
    supplier = Supplier(name, location)
    supplier_repository.save_supplier(supplier)
    return redirect('/suppliers')