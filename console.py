import pdb

from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_repository.delete_all_products()
supplier_repository.delete_all_suppliers()

supplier_1 = Supplier("BI SMOLL")
supplier_repository.save_supplier(supplier_1)

product_1 = Product("IRN BRU", "2 Litre", 1.00, 2.00, 27, "Ambient", supplier_1)
product_repository.save_product(product_1)







pdb.set_trace()