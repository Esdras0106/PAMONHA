import os
os.system("cls || clear")
import time

pares = 0
impares = 0

print(f"ÍNICIO DO PROGRAMA")

for i in range(1,6):
    time.sleep(0.3)
    numero = int(input(f"\nDigite o número: "))
    if numero %2 == 0:
       pares += 1 
    else:
       impares += 1

print(f"\n==FIM DO PROGRAMA==")

print(f"\n Nº de pares: {pares}")
print(f" Nº de ímpares: {impares}")
