import os 
os.system("cls || clear")

listagem = []
QUANTIDADE_NUMEROS = 4

for i in range (QUANTIDADE_NUMEROS):
    numero = float(input("Digite um número: "))
    listagem.append(numero) 

print()
for numero in listagem: 
    print(numero)
    
maior =  max(listagem)
menor =  min(listagem)    
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
