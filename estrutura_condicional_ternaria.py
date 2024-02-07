saldo = 200
saque = 50

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")