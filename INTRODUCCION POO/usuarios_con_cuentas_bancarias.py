class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.accounts = {
      "comprobación": BankAccount(int_rate=0.02, balance=0),
      "ahorros": BankAccount(int_rate=0.02, balance=0),
      "rut_ira": BankAccount(int_rate=0.02, balance=0),
      "ira": BankAccount(int_rate=0.02, balance=0), 
    }

  def hacer_deposito(self, amount, type):
    self.accounts[type].balance += amount
    return self

  def hacer_retiro(self, amount, type):
    self.accounts[type].balance -= amount
    return self

  def transferir_dinero(self, type, other_user, other_user_type, amount):
    self.accounts[type].balance -= amount
    other_user.accounts[other_user_type].balance += amount
    return self

  def mostrar_saldo_usuario(self, type):
    print(f"User: {self.name}, balance: ${self.accounts[type].balance}")



# Objeto de cuenta bancaria

class BankAccount:
  def __init__(self,int_rate=0.02, balance=0):
    self.int_rate = int_rate
    self.balance = balance

  def deposito(self, amount):
    self.balance += amount
    return self

  def retirar(self, amount):
    if self.balance > 0:
      self.balance -= amount
      return self
    else:
      self.balance -= 5
      print(f"Fondos insuficientes: cobrando una tarifa de $ 5")
      return self

  def mostrar_información_de_la_cuenta(self):
      print(f" balance: ${self.balance}")

  def rendimiento_interés(self):
    if self.balance > 0:
      self.balance += self.balance * self.int_rate
      return self
    else:
      return self


user1 = User("Alex Arce", "a.l.e.x_91@hotmail.com")
user2 = User("Fabian Arce", "rf.arce@hotmail.com")
user3 = User("Melissa Arce", "melimosa678@hotmail.com")

user1.hacer_deposito(1000,"comprobación").hacer_deposito(1000,"comprobación").hacer_deposito(1000,"comprobación").hacer_retiro(1000,"comprobación").transferir_dinero("comprobación",user3,"comprobación",100).mostrar_saldo_usuario("comprobación")
user2.hacer_deposito(10000,"ahorros").hacer_deposito(1000,"comprobación").hacer_retiro(2000, "ahorros").mostrar_saldo_usuario("ahorros")
user2.mostrar_saldo_usuario("comprobación")
user3.hacer_deposito(5000000, "ira").hacer_deposito(70000000, "comprobación").hacer_retiro(10000,"comprobación").hacer_retiro(10000, "comprobación").hacer_retiro(10000, "comprobación").mostrar_saldo_usuario("ira")
user3.mostrar_saldo_usuario("comprobación")