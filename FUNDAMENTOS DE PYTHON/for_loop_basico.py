# 1-Básico: imprime todos los números enteros del 0 al 150.

# def numeroprimo(numero):
#     arreglo = []
#     for i in range(0, numero):
#         arreglo.append(i)
#     return arreglo
# print(numeroprimo(151))


# 2-Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

# def numeroprimo(numero):
#     arreglo = []
#     for i in range(1, numero):
#         if i % 5 == 0:
#             arreglo.append(i)
#     return arreglo
# print(numeroprimo(1000))


# 3-Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5,
# imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".

# def numeroprimo(numero):
#     arreglo = []
#     for i in range(1, numero):
#         if i % 5 == 0:
#             print(i, "Coding")
#         if i % 10 == 0:
#             print(i, "Coding Dojo")
#     return arreglo
# print(numeroprimo(100))

# 4-Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.



# listSum = 0
# for number in range(0, 500000, 3):
#     listSum += number
# print(f"Suma total de la lista = {listSum}")

    
           


# 5-Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.


# listSum = 0
# for number in range(2018, 0, -4):
#     listSum += number
# print(f"Suma total de la lista = {listSum}")

# y = 2018
# while y > 0:
#     print(y)
#     y = y - 4
#     if y == 0:
#         break
# else:
#    print("Cuenta regresiva de a 4")


# 6-Contador flexible: establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. 
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

# lowNum = 2
# highNum = 9
# mult = 3

# for f in range(lowNum, highNum + 1):
#     if f % mult == 0:
#         print(f)