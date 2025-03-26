import os
os.system("cls || clear")

contador = 0
quantidade = 0

while True: 
    nota = float(input(f"Informe a nota: "))    
        
    if nota < 0:
        print("""Número inválido, informe um número inteiro.
    Ex: 1 , 3 , 5""")
        break       
        
    contador +=1 
    quantidade += nota 

media = quantidade /contador

print(f"Média: {media}")
    



print("FIMSE")