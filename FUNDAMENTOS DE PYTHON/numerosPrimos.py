def numeroprimo(numero):
    arreglo = []
    for i in range(1, numero):
        if i % 3 == 0:
            arreglo.append(i)
    return arreglo

print(numeroprimo(30))