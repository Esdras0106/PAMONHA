import os
import time
os.system("cls || clear")

print("CONTAGEM RERESSIVA")

i = int(input(f"Informe o valor: "))
for i in range(i,-1,-2):
    time.sleep(1)
    print(f"\n Pares: {i}")