import os
from unittest import case
os.system("clear")

quantidade_de_parcelas = int(input("Quantidade de Parcelas: "))
total_a_pagar = float
valor_do_produto = float(input("Valor do Produto: "))
forma_de_pagamento = str(input("""
1 - Á VISTA                               
2 - PARCELADO 
Informe a forma de Pagamento: """))

#Entrada
match valor_do_produto:
    case 1:
         desconto = valor_do_produto * 0.10
    case 2:
        ...
    case _:
        print("Operação Inválida.")

match forma_de_pagamento:
    case"A vista":
        total_a_pagar == desconto
    case"Parcelado":
        total_a_pagar == valor_do_produto / quantidade_de_parcelas
         
total_a_pagar == desconto    

print(f"\nValor do Produto: {valor_do_produto}")
print(f"\nForma de pagamento: {forma_de_pagamento}")
print(f"\nDesconto: {desconto}")
print(f"Total a pagar: {total_a_pagar}")
