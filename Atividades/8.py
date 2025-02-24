import os
os.system("clear")

login_usado = "Esdras12"
senha_usada = "Pamonha"
login = str(input("Login: "))
senha = str(input("Senha: "))

if  login and senha == login_usado and senha_usada:
    print("Seja bem vindo !")
else:
    print("Login e/ou senha incorretos")

