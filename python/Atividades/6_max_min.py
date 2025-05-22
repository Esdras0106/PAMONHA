import os
os.system("clear")

primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))

maior = max(primeiro_valor, segundo_valor)
menor = min(primeiro_valor, segundo_valor)

print(f"\nPrimeiro valor: {primeiro_valor} ")
print(f"\nSegundo valor: {segundo_valor}")
print(f"\nMaior: {maior}")
print(f"\nMenor: {menor}")