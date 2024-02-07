MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

 #primeiro exemplo
idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("maior de idade, pode tira a CNH. ")

if  idade < MAIOR_IDADE:
    print("menor e idade, Não pode tira a CNH.")


 # segundo exemplo
if idade >= MAIOR_IDADE:
    print ("Maior de idade pode tira")
else:
    print("Menor de idade Não pode tira CNH ")    


# terceiro exemplo

if idade >= MAIOR_IDADE:
    print ("Maior de idade pode tira")
elif idade == IDADE_ESPECIAL:
    print("pode fazer so teorica")
else:
    print("Menor de idade Não pode tira CNH ") 
