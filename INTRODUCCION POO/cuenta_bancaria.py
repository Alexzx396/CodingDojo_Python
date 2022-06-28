class BankAccount:
  def __init__(self, nombre, tasa_interna=0.01, balance=0):
    self.nombre= nombre
    self.tasa_interna = tasa_interna
    self.balance = balance

  def hacer_deposito(self, amount):
    self.balance += amount
    return self

  def hacer_retiro(self, amount):
    if self.balance > 0:
      self.balance -= amount
      return self
    else:
      self.balance -= 5
      print(f"Fondos insuficientes: cobrando una tarifa de $ 5")
      return self

  def mostrar_saldo_usuario(self):
       print(f"User: {self.nombre}, balance: ${self.balance}")


  def rendimiento_interés(self):
    if self.balance > 0:
      self.balance += self.balance * self.tasa_interna
      return self
    else:
      return self

account1 = BankAccount("Alex Arce")
account2 = BankAccount("Fabian Arce")
account1.hacer_deposito(400).hacer_deposito(100).hacer_deposito(300).hacer_retiro(100).rendimiento_interés().mostrar_saldo_usuario()
account2.hacer_deposito(50).hacer_deposito(100).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).hacer_retiro(100).rendimiento_interés().mostrar_saldo_usuario()