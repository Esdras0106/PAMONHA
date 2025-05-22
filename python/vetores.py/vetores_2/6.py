import os
os.system("cls || clear")

lista_pratos = []
preco_pratos = []
soma = 0
preco = 0


while True:
    print(f"""\tcodigo        \tprato             \tvalor    
            1           Picanha                 R$ 25,00
            2           lasanha                 R$ 20,00
            3           Strogonoff              R$ 18,00
            4           Bife acebolado          R$ 15,00
            5           Pão com ovo             R$ 5,00
          """)
    opcao = int(input("Informe o número do seu pedido: "))
        
    match opcao:
        
        case 1:
            prato = (f"Prato escolhido: Picanha")
            preco = 40
        case 2:
            prato = (f"Prato escolhido: Lasanha")
            preco = 30
        case 3:
            prato = (f"Prato escolhido: Strogonoff")
            preco = 25
        case 4:
            prato = (f"Prato escolhido: Bife acebolado")
            preco = 20
        case 5:
            prato = (f"Prato escolhido: Pão com ovo")
            preco = 18
        case _:
            print(f"Opção inválida \nTente novamente.\n")    
    soma += preco
    if opcao >=1 and opcao <=5:   
        lista_pratos.append(prato)
        preco_pratos.append(preco)
    
            
    continuar = (input("Deseja escolher outro prato ? \nDigite 'S' ou 'n': ")).lower()
    if continuar == "n":
        break
    os.system("cls || clear")
    
    if sum(preco_pratos) == 0:
        print(f"\nNenhume prato foi selecionado.")
    else: 
        print(f"\n= PRATOS ESCOLHIDOS =")
        for i, prato in enumerate(lista_pratos, start=1):
            print(f"{i}º prato: {prato}")

    print(f"\nTotal: {sum(preco_pratos): .2f}")