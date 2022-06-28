#1 Cuenta regresiva: crea una función que acepta un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
#Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]

# def countdown(num):
#     new_list = []
#     for i in range(num, -1, -1):
#         new_list.append(i)
#     return new_list    
# print(countdown(5))


#2 Imprimir y devolver: crea una función que recibe una lista con dos números. Imprime el primer valor y devuelve el segundo.
#Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

# def parametro(alist):
#     print(alist[0])
#     return(alist[1])

# parametro([1,2])
# devolver = parametro([1,2])
# print(devolver)


#3 Primero más longitud: crea una función que acepta una lista y devuelve la suma del primer valor de la lista, más la longitud de la lista.
#Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +longitud: 5)

# def parametro(lista):
#     sum = lista[0] + len(lista)
#     return(sum)

# confirm_return = parametro([1,2,3,4,5])
# print(confirm_return)



#4 Valores mayores que el segundo: escribe una función que acepta una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
#  Imprime cuantos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, tiene que la función devuelva False
#  Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#  Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver Falso


# def parametro(alist):
#     if len(alist) < 2:
#         return False
#     new_list = []
#     for i in range(len(alist)):
#         if alist[i] > alist[1]:
#             new_list.append(alist[i])
#     print(len(new_list))
#     return new_list

# confirm_return = parametro([5,2,3,2,1,4])
# print(confirm_return)



#Esta longitud, ese valor: escribe una función que acepta dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
#Ejemplo: longitud_y_valor(4,7) debe devolver [7,7,7,7]
#Ejemplo: longitud_y_valor(6,2) debe devolver [2,2,2,2,2,2]

# def parametro(size, value):
#     create_list = []
#     for i in range(size):
#         create_list.append(value)
#     return create_list

# Actualizar valores en diccionarios y listas
# print(parametro(6,2))

