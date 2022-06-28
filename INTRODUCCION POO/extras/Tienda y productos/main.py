from tienda import tienda
from productos import Productos

target = tienda("Target")

leche = Productos("leche", 1, "comida")
huevo = Productos("huevo", 2, "comida")
camara = Productos("camara", 100, "tecnologia")
silla = Productos("silla", 30, "muebles")
mesa = Productos("mesa", 200, "muebles")

target.add_product(leche)
target.add_product(huevo)
target.add_product(camara)
target.add_product(silla)
target.add_product(mesa)

target.sell_product(2)

target.inflation(0.19)

target.sell_product(0)

target.product_list[1].print_info()
target.set_clearance("muebles",0.5)

target.sell_product(1)
target.sell_product(1)