import os
os.system("clear")

#Entrada
valor_do_produto = float(input("Valor do Produto: "))
forma_de_pagamento = int(input("""
1 - A vista                              
2 - Parcelado 
Informe a forma de Pagamento: """))

match forma_de_pagamento:
    case 1:
        #Aplicando o desconto.
        desconto = valor_do_produto * 0.10
        total_a_pagar = valor_do_produto - desconto
        #Exibido resultados.
        print(f"\nValor do produto: R${valor_do_produto}")
        print(f"Forma de pagamento: à vista")
        print(f"Valor do desconto: R${desconto}")
        print(f"Total da pagar: R${total_a_pagar}")
    case 2:      
         quantidade_de_parcelas = int(input("Digite a quantidade de parcelas: "))
         if quantidade_de_parcelas >= 1 and quantidade_de_parcelas <= 6:
            valor_parcelas = valor_do_produto / quantidade_de_parcelas
         
         #Exibindo resultados.
         
            print(f"\nValor do Produto: R${valor_do_produto}")
            print(f"\nForma de pagamento: Parcelado")
            print(f"\nQuantidade de Parcelas: {quantidade_de_parcelas}")
            print(f"\nValor por Parcela: R${valor_parcelas:.2f}")
            print(f"\nTotal á Prazo: R${valor_do_produto}")                    
         else:
            print("O parcelamento deve ser em até 6 parcelas.")           
    case _:
            print("Operação Inválida.")

