
import os
os.system("cls || clear")


QUANTIDADE_DE_NOTAS = 3
soma = 0

for i in range (QUANTIDADE_DE_NOTAS):
   while True: 
    nota = float(input(f"Informe a nota: "))    
    
    if nota <0 or nota >10 :
        print("""Comando inválido...
tente novamente""")
    else:
        soma+=nota
        break

media = soma / QUANTIDADE_DE_NOTAS 

if media >= 7:
    print("APROVADO.")
elif media <=5:
    print("EM RECUPERAÇÃO.")
else:
    print ("REPROVADO.")
    
print("==FIM==")
