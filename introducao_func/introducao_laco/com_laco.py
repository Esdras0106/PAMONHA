import os
os.system("cls || clear")

print("==ÍNICIO DO PROGRAMA==")

numero = int(input(f"\nInforme o número para a tabuada: "))
for i in range(1,11):
  print(f"{numero} X {i} = {numero * i}")