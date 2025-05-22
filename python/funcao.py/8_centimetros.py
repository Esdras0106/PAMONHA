import os
os.system("cls || clear")


def converter_centimetros(centimetros):
    return centimetros * 100


print(f"\t= CONVERTER METROS PARA CENTÍMETROS =")
metros = float(input(f"\nDigite o número: "))

centimetros = converter_centimetros(metros)

print(f"\t= RESULTADOS =")
print(f"\n{metros} metros é igual a {centimetros} centímetros")
