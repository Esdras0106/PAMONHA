import os
os.system("cls || clear")

while True:
    
    nota = float(input("DIgite a nota: "))

    if nota < 0 or nota >10:
       nota = (input("DIgite a nota: "))
    else:
        print(f"A nota informada foi: {nota}")
        break

print("==FIM==")
