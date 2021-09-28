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
    
    def mark_up(self):
        amount = round(self.sell_price - self.buying_cost, 2)
        return amount

    def show_stock(self):
        if self.stock_count == 0:
            return "This product is out of stock"
        if self.stock_count < 10:
            return "This product is low in stock"
        else:
            return "This product has a safe stock level"