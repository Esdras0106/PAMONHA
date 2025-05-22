import os 
os.system("cls || clear")


soma = 0
while True:
    print("""\tcodigo        \tprato             \tvalor    
            1           picanha                 R$ 25,00
            2           lasanha                 R$ 20,00
            3           strogonoff              R$ 18,00
            4           bife acebolado          R$ 15,00
            5           pão com ovo             R$ 5,00     
                    """)

    pedido = int(input("Informe o número do seu pedido: "))
        
    match pedido:
        case 1:
            escolha = "Picanha "
            preco = 25
        case 2:
            escolha = "Lasanha"
            preco = 20
        case 3:
            escolha = "Strogonoff"
            preco = 18
        case 4:
            escolha = "Bife acebolado"
            preco = 15
        case 5:
            escolha = "Pão com ovo " 
            preco = 5
        case _:
            escolha = "Opção inválida."
            preco = 0
    soma += preco 
    continuar = (input(f"Deseja mais algum item ? \nDigite 'S' ou 'N': ")).lower()
    if continuar == "n": 
        break
  

print(f"Prato escolhido: {escolha}")
print(f"Valor a ser pago: {soma}")
    
        