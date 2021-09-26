from flask import Flask, render_template, request, redirect, Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

supplier_blueprint = Blueprint("suppliers", __name__)

@supplier_blueprint.route('/suppliers')
def suppliers():
    suppliers = supplier_repository.select_all_suppliers()
    return render_template("/suppliers/index.html", suppliers = suppliers)