# 1. TAREA: imprime "Hola, mundo"
tarea = "hola, mundo"
print(tarea)

# 2. imprime "Hola, Noelle" con el nombre en una variable
tarea = "hola"
name = "ALex"
print(tarea +", "+ name)	# con una coma
print(tarea + name)	# con un +

# 3. imprimir "Hola 42!" con el número en una variable
tarea = "hola"
print(tarea , 3)	# con una coma
print(tarea + str(7))	# con una +	-- este debería arrojar un error!

# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Amo comer {} y {}." .format(fave_food1 , fave_food2 )) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f

