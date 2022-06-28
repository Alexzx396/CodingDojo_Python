# Ninja Assignment

class ninja:
    def __init__(self, name, apellido, mascotas, premio, comida_mascotas, salud):
        self.name = name
        self.apellido = apellido
        self.mascotas = mascotas
        self.premio = premio
        self.comida_mascotas = comida_mascotas
        self.salud = salud
        self.energia = 100

    def caminar(self):
        self.salud += 5
        self.energia -= 25
        return self

    def alimentar(self):
        self.salud -= 5
        return self

    def bañar(self):
        self.salud -= 5
        return self

    def displayHealth(self):
        print("\nNinja: " + str(self.name) +  "\nSalud: " + str(self.salud) + "\nenergia: " + str(self.energia))

# Mascota Assignment

class mascota(ninja):
    def __init__(self, name, salud):
        super().__init__(name, salud)
        self.salud = salud

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        return self

    def jugar(self):
        self.salud += 5
        return self

    def display_health_mascota(self):
         super().displayHealth()
         print("I am a dragon")
         return self  



# Case 1
ninja_one = ninja("Alex", "Arce", "Thiago", "Sobar lomo", "Hueso", 100)
ninja_one.alimentar().caminar().bañar().displayHealth()








