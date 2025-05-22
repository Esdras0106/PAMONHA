import os 
from dataclasses import dataclass
os.system("cls || clear")

def limpar():
    os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_admissão: int
    matricula: int
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_nascimento: int
    endereco: str

QUANTIDADE_F = 3
QUANTIDADE = 3
listagem = []
listagem_f = []

for i in range (QUANTIDADE):
    print(f"\t= Solicitando Dados do Cliente =")
    cliente = Cliente(
            nome = input(f"\nDigite o nome do cliente: "),
            data_nascimento = int(input("Digite a data de nascimento do cliente: ")),
            endereco = input("Digiet o endereço do cliente: ")
        )   
    listagem.append(cliente)
    limpar()

for i in range (QUANTIDADE_F):
    print(f"\t= Solicitando Dados do Funcionário =")
    funcionario = Funcionario(
                nome = input(f"\nDigite o nome do funcionário: "),
                data_admissão = input("Informe a data de admissão do funcionário: "),
                matricula = input("Digite a matrícula do funcionário: "),
                endereco = input("Digite o endereço do funcionário: ")
            )
    listagem_f.append(funcionario)
    limpar()


nome_arquivo = "Clientes.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_cliente:
        for cliente  in listagem:
            arquivo_cliente.write(f"\nNome do cliente: {cliente.nome}\nData de nascimento: {cliente.data_nascimento}\nEndereço: {cliente.endereco}")
print(f"\t\nSalvando . .  .")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado")

nome_arquivo = "Funcionários.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivo_funcionario:
    for funcionario  in listagem_f:
            arquivo_funcionario.write(f"\nNome do funcionário: {funcionario.nome}\nData de admissão: {funcionario.data_admissão}\nMatrícula: {funcionario.matricula}\nEndereço: {funcionario.endereco}")
print(f"\t\nSalvando . .  .")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado")


print(f"\n*Dados salvos com sucesso*")