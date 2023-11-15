from datetime import date
from current_account import Current_account
from saving_account import Saving_account
from owner import Owner
from account import Account

#Duenio

josue_garcia = Owner(15, "Josue", "Garcia", "1729222784",date(2004, 10, 15),
                      "Las Casas", "delvallejosue3@gmail.com")

#Cuenta

banco_pichincha = Account(1, "2209075624", 1500.56, josue_garcia, 0)

#Cuenta Ahorros

pichincha_ahorros = Saving_account(2, "22090756", 900, josue_garcia, 300, 0)

#Cuenta Corriente

pichincha_corriente = Current_account(3, "22090758", 300, josue_garcia, 0, 200)

print("| Informacion Cliente |")
print(josue_garcia)
print("Cuenta:",banco_pichincha.get_account_id(), "\n")

print("| Informacion Cuentas |")
print("----- Cuenta ahorros ------")
print("Numero de cuenta:", pichincha_ahorros.get_account_id())
print("Saldo Cuenta ahorros:", pichincha_ahorros.get_balance())
print("Limite de transaccion diaria:", pichincha_ahorros.get_limit_transaction())
print()

print("----- Cuenta corriente ------")
print("Numero de cuenta:", pichincha_corriente.get_account_id())
print("Saldo Cuenta Corriente:", pichincha_corriente.get_balance())
print()

print("| Informacion Depositos |")
banco_pichincha.deposit(500.55)
print("Saldo despues del deposito:", banco_pichincha.get_balance())
banco_pichincha.deposit(100.30)
print("Saldo despues del deposito:", banco_pichincha.get_balance())
banco_pichincha.deposit(1500.79)
print("Saldo despues del deposito:", banco_pichincha.get_balance())
print()

print("| Informacion Retiros |")

pichincha_ahorros.set_limit_transaction(200)
pichincha_ahorros.withdraw(35.67)
print("Saldo cuenta ahorros:", pichincha_ahorros.get_balance())
pichincha_corriente.withdraw(100.99)
print("Saldo cuenta corriente:", pichincha_corriente.get_balance())

print("| Informacion Cheques |")
print("Saldo cuenta corriente:", pichincha_corriente.get_balance())
pichincha_corriente.issue_check(30)
print("Saldo cuenta corriente:", pichincha_corriente.get_balance())




