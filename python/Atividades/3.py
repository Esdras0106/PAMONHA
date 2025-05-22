import os 
os.system ("clear") # Limpar o terminal

primeira_nota = float (input ("1ª nota: "))
segunda_nota = float (input ("2ª nota: "))
terceira_nota = float (input ("3ª nota: "))

soma = primeira_nota + segunda_nota + terceira_nota 
media = soma / 3  

print(f"Média: 5")

if  media < 7:
    print("REPROVADO!")
else:
    print("APROVADO!")

