import os
os.system("clear")

nome_do_empregado = (input("Nome do empregado: "))
idade = int(input("Idade do empregado: "))
tempo_trabalhado = int(input("Tempo de Contribuição: "))
codigo = int(input("Informe o seu código: "))

match idade:
    case 65 :    
        
        if tempo_trabalhado >= 30:
            print("Requerer aposentadoria.")
        else:
            print("Não requerer aposentadoria.")
            
    case _:
            if idade <65:
                print("Não requerer aposentadoria.")
            elif idade >=65:
                print("Requerer aposentadoria.")
            else:
                print("Não requerer aposentadoria")
            
print(f"\nNome do empregado: {nome_do_empregado}")
print(f"\nIdade: {idade}")
print(f"\nTempo de Contribuição: {tempo_trabalhado}")
print(f"\nCódigo do empregado: {codigo}")
