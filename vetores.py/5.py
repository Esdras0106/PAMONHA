import os 
os.system("cls || clear")

listagem = []
QUANTIDADE_NUMEROS = 6

def pares_impares(listagem):
    impar = 0
    par = 0
    for numero in listagem: 
        if numero % 2 ==0 :
            par += 1
        else:
            impar += 1    
    return par, impar

print(f"\n\t= Solicitando Dados =")
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input("Digite um número: "))
    listagem.append(numero)       

par, impar = pares_impares(listagem)

print(f"\n\t= Mostrando resultados =")
for i, numero in enumerate(listagem, start=1):
    print(f"{i}º número: {numero}")
    
print(f"Par: {par}")
print(f"Ímpar: {impar}")
