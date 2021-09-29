from flask import Flask, render_template, request, redirect, Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

supplier_blueprint = Blueprint("suppliers", __name__)

@supplier_blueprint.route('/suppliers') #This displays supplier index
def suppliers():
    suppliers = supplier_repository.select_all_suppliers()
    return render_template("/suppliers/index.html", suppliers = suppliers)

@supplier_blueprint.route('/suppliers/new') #This displays new supplier page
def new_supplier():
    return render_template('/suppliers/new.html')

@supplier_blueprint.route('/suppliers', methods=['POST']) #This sends entered supplier information to supplier page
def create_supplier():
    name = request.form['name']
    location = request.form['location']
    active = request.form['active']
    supplier = Supplier(name, location, active)
    supplier_repository.save_supplier(supplier)
    return redirect('/suppliers')

@supplier_blueprint.route('/suppliers/<id>', methods=["GET"]) #This displays a single supplier
def show_supplier(id):
    supplier = supplier_repository.select_supplier(id)
    return render_template('suppliers/show.html', supplier = supplier)

@supplier_blueprint.route('/suppliers/<id>/edit', methods=['GET']) #This displays an edit page for supplier
def edit_supplier(id):
    supplier = supplier_repository.select_supplier(id)
    return render_template('/suppliers/edit.html', supplier = supplier)

@supplier_blueprint.route('/suppliers/<id>', methods=['POST']) #This sends updated information and goes to supplier page
def update_supplier(id):
    name = request.form['name']
    location = request.form['location']
    active = request.form['active']
    supplier = Supplier(name, location, active, id)
    supplier_repository.update_supplier(supplier)
    return redirect('/suppliers')