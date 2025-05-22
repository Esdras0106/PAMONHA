import os
os.system("cls || clear")

total = 0
soma_f = 0
soma_geral = 0
salarios = 0

while True:    
    print("""Código  |  Descrição
1       |  Adicionar Pessoa    
2       |  Exibir Resultados
3       |  Sair                 """)
    opcao = float(input(f"\nInforme a opção desejada: "))
    
    match opcao:
        case 1:
            idade = (input(f"\nInforme a idade: "))
            sexo = (input("Informe o sexo: ")).lower()
            salario = float(input("Informe o salário: "))
            salarios += salario
            soma_geral += 1 
            total = salarios / soma_geral
            if sexo == "F" and salario >= 5.000:
                soma_f += 1           
            import os
            os.system("cls || clear")
        case 2: 
            import os
            os.system("cls || clear")
            print(f"\nA média de salários do grupo é: {total}")
            print(f"A quantidade de mulheres com salários maior que R$ 5.000,00 é {soma_f}")
            break
        case 3:
            break
        case _:
            print("Opção inválida, tente novamente.")

print(f"\n ==FIM DO PROGRAMA==")
        
            
            
   
     
        