import os
os.system("clear")

primeiro_valor = float(input("Primeiro valor: "))
segundo_valor = float(input("Segundo valor: "))
 
soma = primeiro_valor + segundo_valor
media =  soma / 2
produto = primeiro_valor * segundo_valor

if  primeiro_valor < segundo_valor:
    menor = primeiro_valor
    maior = segundo_valor
else:
    menor = segundo_valor
    maior = primeiro_valor

print("\nExibindo resultados: ")
print(f"\nSoma:  {soma}" ) 
print(f"\nMédia: {media}" ) 
print(f"\nProduto:  {produto}" )
print(f"\nMaior: {maior}")
print(f"\nMenor: {menor}")
