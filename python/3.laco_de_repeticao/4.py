import os
os.system("cls || clear")

while True:
    
    nota = float(input("Digite a nota: "))
    if nota <0 or nota >10:
        nota = float(input("Digite a nota: "))
    else:
        print(f"\nA nota informada foi: {nota}")
        break

media = nota / 2

if media <6 and media >4:
    print("RECUPERAÇÃO!")
elif media <4:
    print("REPROVADO.")
else:
    print("APROVADO.")

print(f"Média aritimetica: {media}")
print(f"\n==FIM==-")
