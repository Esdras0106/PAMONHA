import os
import time
os.system("cls || clear")

def limpar():
    os.system("cls || clear")


lista_fun = []
lista_data = []
lista_cpf = []
lista_funcao = []


def adicionar_funcionario(lista_fun):
    nome = input("\nDigite o nome do funcionário que deseja adicionar: ")
    lista_fun.append(nome)
    print(f"\nO nome ({nome}) adicionado com sucesso.")

def fun_cpf(lista_cpf):
    cpf = input("\nDigite o cpf do funcionário que deseja adicionar: ")
    lista_cpf.append(cpf)
    print(f"\nO nome ({cpf}) adicionado com sucesso.")

def fun_data(lista_data):
    data_nasc = input("\nDigite a data que deseja adicionar: ")
    lista_data.append(data_nasc)
    print(f"\nA data ({data_nasc}) adicionado com sucesso.")

def fun_funcao(lista_funcao):
    funcao = input("\nDigite o nome da função do funcionário: ")
    lista_funcao.append(funcao)
    print(f"\nA funcao({funcao}) foi adicionada com sucesso.")


def listar_nomes(lista_fun):
    print(f"\n- Lista dos funcionários -")
    for nome in lista_fun: 
        print(f"\n- {nome}")

def listar_data(lista_data):
    print(f"\n- Lista das Datas -")
    for data_nasc in lista_data: 
        print(f"\n- {data_nasc}")

def listar_cpf(lista_cpf):
    print(f"\n- Lista de CPF -")
    for cpf in lista_cpf: 
        print(f"\n- {cpf}")

def listar_funcao(lista_funcao):
    print(f"\n- Lista das funções -")
    for funcao in lista_funcao: 
        print(f"\n- {funcao}")

def excluir_nome(lista_fun):
    listar_nomes(lista_fun)
    nome_remove = input(f"\nDigite o nome que deseja remover: ")
    if nome_remove in lista_fun: 
        lista_fun.remove(nome_remove)
        print(f"O funcionário '{nome_remove}' foi removido da lista com sucesso.")
    else:
        print(f"O funcionário {nome_remove} não foi encontrado na lista.")


def atualizar_nome(lista_fun):
    listar_nomes(lista_fun)
    nome_antigo = input(f"\nDigite o nome do funcionário que deseja atualizar: ")
    novo_nome = input(f"\nDigite o novo nome para '{nome_antigo}': ")
    if nome_antigo in lista_fun:
        indice = lista_fun.index(nome_antigo)
        lista_fun[indice] = novo_nome
        limpar()
        print(f"O nome '{nome_antigo}' foi atualizado para {novo_nome}.")
    else:
        print(f"\nO funcionário '{nome_antigo}' não foi encontrado.")

def atualizar_data(lista_data):
    listar_data(lista_data)
    data_antiga = input(f"\nDigite a data de nascimento que deseja atualizar: ")
    nova_data = input(f"\nDigite uma nova data para '{data_antiga}': ")
    if data_antiga in lista_data:
        indice = lista_data.index(data_antiga)
        lista_data[indice] = nova_data
        limpar()
        print(f"A data '{data_antiga}' foi atualizada para {nova_data}.")
    else:
        print(f"\nA data '{data_antiga}' não foi encontrada.")

def atualizar_cpf(lista_cpf):
    listar_cpf(lista_cpf)
    cpf_antigo = input(f"\nDigite o cpf que deseja atualizar: ")
    novo_cpf = input(f"\nDigite o novo cpf para '{cpf_antigo}': ")
    if cpf_antigo in lista_cpf:
        indice = lista_cpf.index(cpf_antigo)
        lista_cpf[indice] = novo_cpf
        limpar()
        print(f"O cpf '{cpf_antigo}' foi atualizado para {novo_cpf}.")
    else:
        print(f"\nO cpf '{cpf_antigo}' não foi encontrado.")

def atualizar_funcao(lista_funcao):
    listar_funcao(lista_funcao)
    funcao_antiga = input(f"\nDigite o nome da função que deseja atualizar: ")
    nova_funcao = input(f"\nDigite o novo nome da função '{funcao_antiga}': ")
    if funcao_antiga in lista_funcao:
        indice = lista_fun.index(funcao_antiga)
        lista_fun[indice] = nova_funcao
        limpar()
        print(f"A função '{funcao_antiga}' foi atualizada para {nova_funcao}.")
    else:
        print(f"\nA função '{funcao_antiga}' não foi encontrada.")

# Mostrando menu.
while True:
    print("""
- Gerenciador de nomes -
1- Adicionar Funcionário
2- Listar funcionários
3- Listar datas
4- Listar cpf          
5- Listar funções
6- Atualizar funcionário
7- Atualizar CPF          
8- Atualizar Data
9- Atualizar Função                                                  
10- Remover
11- Adicionar uma data de nascimento
12- Adicionar um cpf
13- Adicionar uma função          
14- Sair          
""")
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_funcionario(lista_fun)
        case 2:
            listar_nomes(lista_fun)
        case 3:
            listar_data(lista_data)
        case 4:
            listar_cpf(lista_cpf)        
        case 5:
            listar_funcao(lista_funcao)        
        case 6:
            atualizar_nome(lista_fun)
        case 7:
            atualizar_cpf(lista_cpf)
        case 8:
            atualizar_data(lista_data)
        case 9:
            atualizar_cpf(lista_cpf)    
        case 10:
            atualizar_funcao(lista_funcao)
        case 11:
            fun_data(lista_data)
        case 12:
            fun_cpf(lista_cpf)
        case 13:
            fun_funcao(lista_funcao)
        case 14:
            os.system("cls || clear")
            print(f"\nPrograma Finalizado.")
            break
        case _:
            print("Opção inválida.")

    if opcao !=1: 
        time.sleep(3.5)        
        os.system("cls || clear")