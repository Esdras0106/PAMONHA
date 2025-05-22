import os
os.system("cls || clear")

media = 0

while True:
    
    nota = float(input("DIgite a nota: "))

    if nota < 0 or nota >10:
       nota = (input("DIgite a nota: "))
    else:
        print(f"A nota informada foi: {nota}")
        break

if nota < 6 and nota >4:
    print("RECUERAÇÃO.")
else:
    print("APROVADO.")
    

print("==FIM==")
