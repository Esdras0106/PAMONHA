import os 
os.system("clear")

nome_do_estagiario = str(input("Nome do Estagiário: "))
quantidade_de_faltas = int(input("Quantidade de faltas: ")) 
comportamento_do_funcionario =str(input("Comportamento dentro da empresa: "))

if comportamento_do_funcionario =="ruim":
     print("Funcionário mal comportado")    
elif comportamento_do_funcionario == "bom":
     print("Funcionário bem portado")
else:
     print("Funcionario esforçado")