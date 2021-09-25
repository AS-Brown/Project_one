from flask import Flask, render_template, request, redirect, Blueprint
from models.product import Product
import repositories.product_repository as product_repository

product_blueprint = Blueprint("products", __name__)

