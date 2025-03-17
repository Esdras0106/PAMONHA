import os 
os.system("cls || clear")
import time

valor = 0
for i in range(1,6):
    time.sleep(0.1)
    print(f"{valor} + {i} = {valor + i }")
    soma = int(input(f"Informe o {i+1}º número inteiro para a soma: "))
    valor = valor + soma

print(f"Soma = {valor}")