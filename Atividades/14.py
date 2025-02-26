import os
os.system("clear")

#Entrada
mes = input("Mês: ")

#Processamento
match mes:
    case"1":
      mes = ("janeiro")
    case"2":
      mes = ("fervereiro")
    case"3":
      mes = ("março")
    case"4":
      mes = ("abril")
    case"5":
      mes = ("maio")
    case"6":
      mes = ("junho")
    case"7":    
      mes = ("julho")
    case "8":
      mes = ("agosto")
    case "9":
      mes = ("setermbro")
    case "10":
      mes = ("outubro")
    case "11":
      mes = ("novembro")
    case "12":
      mes = ("dezembro")

    case _: 
      mes = "opção inválida."
  
#Saída
print(f"\nMês: {mes}")

