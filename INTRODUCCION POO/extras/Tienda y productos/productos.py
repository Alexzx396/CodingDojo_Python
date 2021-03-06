class Productos:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        elif not is_increased:
            self.price += -1 * self.price * percent_change
    
    def print_info(self):
        print(f"nombre: {self.name}")
        print(f"Categoria: {self.category}")
        print(f"Precio: {self.price}")