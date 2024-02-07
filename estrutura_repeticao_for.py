texto = input("informe um texto :")

VOGAIS = "AEIOU"

# Exemplo ultilizando um iteravel
for letra in texto:
    if letra.upper()in VOGAIS:  #upper é para trasformar um Maiúscula
        print(letra, end="")
else:
    print("Executa no final do laço")  


# Exemplo utilizado a finçao built-in range
for numero in range (0, 51, 5):
    print(numero, end=" ")