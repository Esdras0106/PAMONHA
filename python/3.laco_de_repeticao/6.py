import os 
os.system("cls || clear")

login_criado = "Esdras"
senha_criada = "123"
contador = 0

for i in range (1,4):
    login = (input("Informe o login: "))
    senha = (input("Insira a senha: "))
    
    if login == login_criado and senha == senha_criada:
        print("Acesso liberado.")
        break
    else: 
        print(f"Login e/ou senha incorretos. \n")
        contador += 1
    if contador == 3:
        print("Número de tentativas excedido, tente novamente mais tarde.")

print(f"\n  Programa Finalizado.")