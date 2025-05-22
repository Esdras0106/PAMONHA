import os 

def limpeza():
    os.system("cls || clear")

def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma / 2
    return media

limpeza ()
primeiro_numero = int(input(f"\nDigite o 1° número: "))
limpeza()
segundo_numero = int(input(f"\nDigite o 2° número: "))

media = calcular_media(primeiro_numero, segundo_numero)

if media <5:
    print(f"\nEm recuperação !")
elif media >=5:
    print(f"\nAprovado !")
else:
    print(f"\nREPROVADO !")




print(f"Média: {media}")