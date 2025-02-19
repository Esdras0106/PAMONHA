import os 
os.system ("clear") # Limpar o terminal

#se idade <12
#escreval("SOMENTE COM A PERMISSÃO DOS PAIS!")
#sena
#escreval("ACESSO LIBERADO")
#fimse

idade = int(input("Idade: "))
                  
if   idade < 12:
    print("ACESSO BLOQUEADO")
elif idade < 18:
     print("SOMENTE COM A PERMISSÃO DOS PAIS!")
else:
     print("ACESSO LIBERADO")