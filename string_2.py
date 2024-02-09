nome = "Leonardo"
idade= 26
profissao = "Programador"
linguagem = "python"
saldo = 45.581                        

dados = {"nome": "Leonardo", "idade": 26}

print("Nome: %s Idade: %d" % (nome,idade)) #má pratica / old style%
print("Nome: {} Idade: {}" .format (nome,idade)) #não é muito/ recomendado format


print("Nome: {0} Idade: {1}".format (nome,idade)) #Boa pratica/ f-string
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format (idade,nome)) #Boa pratica/ f-string - aqui é o mesmo metodo só que pediu mais dados
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) #Boa pratica/ f-string 
print("Nome: {name} Idade: {age}".format(age=idade, name=nome)) #Boa pratica/ f-string  
print("Nome: {nome} Idade: {idade}".format(**dados)) #Boa pratica/ f-string 

# formatar string
print(f"Nome: {nome} Idade:{idade}")
print(f"Nome: {nome} Idade: {idade} saldo: {saldo:10.2f}")