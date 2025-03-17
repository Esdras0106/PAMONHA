import os
os.system("cls || clear")
import time

print(f"ÍNICIO DO PROGRAMA")

media = 0

for i in range(1,5):
    time.sleep(0.2)
    nota = float(input(f"\nDigite a {i}ª nota: "))
    media += nota / 4

if media < 7  >4 :
    print("RECUPERAÇÃO!")
elif media <4: 
    print("REPROVADO!") 
else:
    print("APROVADO.")
    

print(f"Média: {media}")

print(f"\n==FIM DO PROGRAMA==")
