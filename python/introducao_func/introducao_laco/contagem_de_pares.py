import os
import time
os.system("cls || clear")

print("CONTAGEM DE NÚMEROS PARES")

i = int(input(f"Informe os pares: "))
for i in range(100,121,2):
    time.sleep(0.5)
    print(f"\n Pares: {i}")
print(f"  NÚMERO USADO:  {i}")