from flask import Flask, render_template, request, redirect, Blueprint
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

supplier_blueprint = Blueprint("suppliers", __name__)

