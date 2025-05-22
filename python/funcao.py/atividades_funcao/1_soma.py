import os

def logo_senai():
    os.system("cls || clear")   
    print(f"\t== SENAI DENDEIZEIROS ==")
    
    

def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero


logo_senai()    
primeiro_numero = int(input(f"\nDigite o primeiro número: "))

logo_senai()    
segundo_numero = int(input(f"\nDigite o segundo número: "))

soma = somar(primeiro_numero, segundo_numero)

logo_senai()    # Chamando a função
print(f"\nPrimeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Soma : {soma}")
