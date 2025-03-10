import os
os.system("clear")

sexo = str(input("Digite o sexo da pessoa: "))
altura = float(input("Informe a Altura da pessoa: "))

match sexo:    
        case "M" | "m":
            peso_ideal = (72.7 * altura) - 58
            print(f"\nPeso ideal: {peso_ideal : .2f}")
        case "F" | "f:":
            peso_ideal = (62.1 * altura) - 44.7
            print(f"\nPeso ideal: {peso_ideal : .2f}")
        case _:
            print("Opção inválida.")
            
            