import os 
os.system("clear")

primeira_nota = float(input ("1ª nota: "))
segunda_nota = float(input ("2ª nota: "))

soma = primeira_nota + segunda_nota
media = soma  /3
print("Média: ")
if  media < 5:
    print("REPROVADO")
elif media == 4:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")