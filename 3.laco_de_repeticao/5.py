import os 
os.system("cls || clear")

login_criado = "Esdras"
senha_criada = "123"

while True:
    login = (input("Informe o login: "))
    senha = (input("Insira a senha: "))
    
    if login == login_criado and senha == senha_criada:
        print("Acesso liberado.")
        break
    else: 
        print(f"Login e/ou senha incorretos. \n")
        

print("==FIM DO PROGRAMA==")