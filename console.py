import pdb

from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

supplier_1 = Supplier("BI SMOLL")
supplier_repository.save_supplier(supplier_1)

pdb.set_trace()