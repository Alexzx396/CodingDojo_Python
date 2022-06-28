
class User:
    def __init__(self, nombre, email):
        self.nombre= nombre
        self.email= email
        self.account_balance = 0

    def hacer_deposito(self, amount):
      self.account_balance += amount
      return self

    def hacer_retiro(self, amount):
      self.account_balance -= amount
      return self

    def  transferir_dinero(self, other_user, amount):
      self.account_balance -= amount
      other_user.account_balance += amount
      return self

    def mostrar_saldo_usuario(self):
      print(f"User: {self.nombre}, balance: ${self.account_balance}")


user1 = User("Alex Arce", "a.l.e.x_91@hotmail.com")
user2 = User("Fabian Arce", "rf.arce@hotmail.com")
user3 = User("Melissa Arce", "melimosa678@hotmail.com")

user1.hacer_deposito(300).hacer_deposito(8000).hacer_deposito(4000).hacer_retiro(1000).mostrar_saldo_usuario()
user2.hacer_deposito(10000).hacer_deposito(6000).hacer_retiro(2000).mostrar_saldo_usuario()
user3.hacer_deposito(5000000).hacer_retiro(10000).hacer_retiro(10000).hacer_retiro(10000).mostrar_saldo_usuario()

user1. transferir_dinero(user2, 4000).mostrar_saldo_usuario()
user2.mostrar_saldo_usuario()