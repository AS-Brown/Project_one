import pdb

from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_repository.delete_all_products()
supplier_repository.delete_all_suppliers()

supplier_1 = Supplier("BI SMOLL", "Dundee")
supplier_repository.save_supplier(supplier_1)
supplier_2 = Supplier("DK WODE", "Aberdeen")
supplier_repository.save_supplier(supplier_2)
supplier_3 = Supplier("GREENINGS", "Kilmarnock")
supplier_repository.save_supplier(supplier_3)

product_1 = Product("IRN BRU", "2 Litre", 1.00, 2.00, 27, "Ambient", supplier_1)
product_repository.save_product(product_1)
product_1 = Product("FANTA", "2 Litre", 1.20, 1.75, 22, "Ambient", supplier_1)
product_repository.save_product(product_1)
product_1 = Product("CRISP WHITE", "75ml", 4.35, 5.00, 23, "Alcohol", supplier_2)
product_repository.save_product(product_1)
product_1 = Product("FERN HILL", "75ml", 4.50, 5.50, 24, "Alcohol", supplier_2)
product_repository.save_product(product_1)
product_1 = Product("KILLIE PIE", "150g", 1.00, 1.99, 0, "Chill", supplier_3)
product_repository.save_product(product_1)
product_1 = Product("CURRY PIE", "175g", 1.00, 1.99, 6, "Chill", supplier_3)
product_repository.save_product(product_1)

pdb.set_trace()