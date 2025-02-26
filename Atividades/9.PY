import os 
os.system("clear")

#Match Case substitui if-else-elif

dia = input ("Digite sua idade")

match dia:
     case "Segunda"
     print("Hoje é segunda-feira!")
     case "Terça"
     print("Hoje é terça-feira!")
     case "Quarta"
     print("Hoje é quarta-feira!")
     case "Quinta"
     print("Hoje é quinta-feira!")
     case "Sexta"
     print("Hoje é quinta-feira!")
     case "Sábado" | "Domingo"
     print("Fim De Semana")
case_:
     print("Dia inválido!")

print("Dia")
print("==FIM==")