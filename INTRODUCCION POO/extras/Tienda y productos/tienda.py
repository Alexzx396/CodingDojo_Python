from productos import Productos

class tienda:
    def __init__(self, name):
        self.name = name
        self.product_list = []
    
    def add_product(self, new_product):
        self.product_list.append(new_product)
    
    def sell_product(self, id):
        removed_product = self.product_list.pop(id)
        removed_product.print_info()

    def inflation(self, percent_increase):
        for Productos in self.product_list:
            Productos.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for Productos in self.product_list:
            if Productos.category == category:
                Productos.update_price(percent_discount, False)