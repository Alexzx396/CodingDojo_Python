
class User:
    def __init__(self, nombre, email):
        self.nombre= nombre
        self.email= email
        self.account_balance = 0

    def hacer_deposito(self, amount):
      self.account_balance += amount

    def hacer_retiro(self, amount):
      self.account_balance -= amount

    def mostrar_saldo_usuario(self):
      print(f"User: {self.nombre}, balance: ${self.account_balance}")

    def transferir_dinero(self, other_user, amount):
      self.account_balance -= amount
      other_user.account_balance += amount

user1 = User("Alex Arce", "a.l.e.x_91@hotmail.com")
user2 = User("Fabian Arce", "rf.arce@hotmail.com")
user3 = User("Melissa Arce", "melimosa678@hotmail.com")

user1.hacer_deposito(1000)
user1.hacer_deposito(5000)
user1.hacer_deposito(4000)
user1.hacer_retiro(1000)
user1.mostrar_saldo_usuario()

user2.hacer_deposito(10000)
user2.hacer_deposito(6000)
user2.hacer_retiro(2000)
user2.mostrar_saldo_usuario()

user3.hacer_deposito(5000000)
user3.hacer_retiro(10000)
user3.hacer_retiro(10000)
user3.hacer_retiro(10000)
user3.mostrar_saldo_usuario()

user1.transferir_dinero(user2, 300)
user1.mostrar_saldo_usuario()
user3.mostrar_saldo_usuario()