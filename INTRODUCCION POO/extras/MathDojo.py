class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *nums):
    # tu código aquí
        for n in nums:
            self.result = self.result + n
        return self

    def subtract(self, *nums):
    # tu código aquí
        for n in nums:
            self.result = self.result - n
        return self

    def multiplicar(self, *nums):
    # tu código aquí
        for n in nums:
            self.result = self.result * n
        return self

    def dividir(self, *nums):
    # tu código aquí
        for n in nums:
            self.result = self.result / n
        return self


# crear una instancia:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(f"Resultado x: {x}")	# debería imprimir 5
# ejecuta cada uno de los métodos unas cuantas veces más y verifica el resultado
y = md.subtract(51).add(5).add(25,5,2).subtract(1,2).add(14,80,2,3,52).subtract(2,37,10).multiplicar(2,37,10).result
print(f"Resultado y: {y}")
#ejemplo multiplicar
h = md.multiplicar(2,10).dividir(50).result
print(f"Resultado h: {h}")


