class Product:
    def __init__(self, name, description, buying_cost, sell_price, stock_count, type_of_product, supplier, id = None):
        self.name = name
        self.description = description
        self.buying_cost = buying_cost
        self.sell_price = sell_price
        self.stock_count = stock_count
        self.type_of_product = type_of_product
        self.supplier = supplier
        self.id = id