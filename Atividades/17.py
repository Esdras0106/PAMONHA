import os
os.system("clear")

nome_do_aluno = str(input("Informe o nome do aluno: "))
primeira_nota = float(input("Primeira nota: "))
segunda_nota = float(input("Segunda nota: "))

# Base da Média
media = (primeira_nota + segunda_nota) / 2

if media >= 9:   
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    coneito = "E"     

match conceito:
    case "A"| "B" | "C" :
     print(f"\nConceito: {conceito}")
     print(f"\nAprovado.")
    case "D" | "E":
     print(f"\nConceito: {conceito}")
     print(f"\nReprovado")
    case _:
     print("Opção inválida")

print(f"\nPrimeira nota: {primeira_nota}")    
print(f"\nSegunda nota: {segunda_nota}")
print(f"\nMédia: {media}")
print(f"\nConceito Correspondente: {conceito}")

