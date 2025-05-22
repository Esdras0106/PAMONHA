import os
os.system("clear")

idade = int(input("Digite sua Idade: "))

#Opção 1
if  idade >18 and idade <65:
    resultado = "Voto obrigatório"
else:
    resultado = "Não é obrigado a votar."   

print(f"Idade: {idade}")
print(f"Resultado: {resultado}")