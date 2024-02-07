conta_normal = True
conta_universitaria = False

saldo = 5000
saque= 500
cheque_especial= 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso de cheque especial.")
    else:
        print("Não foi possivel realizar o saque")    
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado")
    else:
        print("Saldo insuficiente!")                