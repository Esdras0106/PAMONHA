import os 
os.system("clear")

#Match Case substitui if-else-elif

dia = int(input("Digite o dia: "))

match dia:
     case 1 :
          print("Hoje é segunda-feira!")
     case 2 :
          print("Hoje é terça-feira!")
     case 3 :
          print("Hoje é quarta-feira!")
     case 4 :
          print("Hoje é quinta-feira!")
     case 5 :
          print("Hoje é quinta-feira!")
     case 6 | 7:
          print("Sábado ou Domingo !")
     case _:
          print("Dia inválido!")


print("==FIM==")