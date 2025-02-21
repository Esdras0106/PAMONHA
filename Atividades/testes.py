import os 
os.system("clear")

nome_do_estagiario = str(input("Nome do Estagiário: "))
quantidade_de_faltas = int(input("Quantidade de faltas: ")) 
comportamento_do_funcionario =str(input("Comportamento dentro da empresa: "))

print("\nAVALIAÇÃO DOS ESTAGIÁRIOS: ")



if   quantidade_de_faltas <10:
     print("Funcionário de alta contrinuição para a empresa")    
else: 
     print("Funcionário de baixa contribuição para a empresa")

if   comportamento_do_funcionario == "ruim":     
     print("Funcionário mal comportado")    
elif comportamento_do_funcionario == "bom":
     print("Funcionário bem portado")
else:
     print("Funcionario esforçado")