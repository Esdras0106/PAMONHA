import os

def logo_senai():
    os.system("cls || clear")   
    print(f"\t== SENAI DENDEIZEIROS ==")
        

def subtrair (primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def produtos(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def medias(primeiro_numero, segundo_numero):
    return primeiro_numero / segundo_numero

logo_senai()    
primeiro_numero = int(input(f"\nDigite o 1º número: "))

logo_senai()    
segundo_numero = int(input(f"\nDigite o 2º número: "))

subtracao = subtrair(primeiro_numero, segundo_numero)
soma = somar (primeiro_numero, segundo_numero)
produto = produtos (primeiro_numero, segundo_numero)
media =  medias(primeiro_numero, segundo_numero)

logo_senai()  
print(f"\nPrimeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Média: {media}")
