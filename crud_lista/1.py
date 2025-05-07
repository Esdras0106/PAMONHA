import os
import time
os.system("cls || clear")



def limpar():
    os.system("cls || clear")

# Lista de nomes.
lista_nomes = []



# Função para mostrar todos os nomes da lista.
def verificar_lista_vazia(lista_nomes):
    if not lista_nomes: # Se a lista NÃO tiver conteúdo, retira o valor 'VERDADEIRO'. 
        return True
    return False # Se a lista possuir algum conteúdo. 

# Função para adicionar.
def adicionar_nome(lista_nomes):
    nome = input("\nDigite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\nO nome ({nome}) adicionado com sucesso.")


# Verificar se a lista está vazia.
def listar_nomes(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return    
    
    print(f"\n- Lista de nomes -")
    for nome in lista_nomes: # Percorre a lista para encontrar o nome informado.
        print(f"\n- {nome}")

# Função para excluir um nonme da lista.
def excluir_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print(f"\nA lista está vazia.")
        return

    listar_nomes(lista_nomes)
    nome_remove = input(f"\nDigite o nome que deseja remover: ")
    if nome_remove in lista_nomes: # Percorre a lista para encontrar o nome informado. 
        lista_nomes.remove(nome_remove)
        print(f"O nome '{nome_remove}' foi removido com sucesso.")
    else:
        print(f"O nome {nome_remove} não foi encontrado.")


#Função para atualizar.
def atualizar_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia.")
        return

    listar_nomes(lista_nomes)
    nome_antigo = input(f"\nDigite o nome que deseja atualizar: ")
    novo_nome = input(f"\nDigite o novo nome para '{nome_antigo}': ")
    if nome_antigo in lista_nomes:
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        limpar()
        print(f"O nome '{nome_antigo}' foi atualizado para {novo_nome}.")
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")



# Mostrando menu.
while True:
    print("""
- Gerenciador de nomes -
1- Adicionar 
2- Listar nomes
3- Atualizar 
4- Remover
5- Sair
""")
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_nome(lista_nomes)
        case 2:
            listar_nomes(lista_nomes)
        case 3:
            atualizar_nome(lista_nomes)
        case 4:
            excluir_nome(lista_nomes)
        case 5:
            os.system("cls || clear")
            print(f"\nPrograma Finalizado.")
            break
        case _:
            print("Opção inválida.")
    if opcao !=1:
        time.sleep(4) 
    os.system("cls || clear")