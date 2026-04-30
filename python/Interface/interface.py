import customtkinter as ctk

# Configuração da aparência
ctk.set_appearance_mode("Dark")

# Função de Cálculo
def CalcularGasto():
    try:
        # Pega os valores, troca vírgula por ponto (caso o usuário digite 5,50) e converte para float
        d = float(distancia.get().replace(',', '.'))
        c = float(consumo.get().replace(',', '.'))
        p = float(preco.get().replace(',', '.'))
        
        # Evita a divisão por zero se o usuário colocar consumo = 0
        if c == 0:
            resultado.configure(text="Erro: O consumo não pode ser zero.", text_color="red")
            return

        # Cálculo
        calculo = (d / c) * p
        resultado.configure(text=f"O preço final da viagem foi de R$ {calculo:.2f}", text_color="green")
        
    except ValueError:
        # Se der erro na conversão (ex: letras ou campo vazio), avisa o usuário sem fechar o app
        resultado.configure(text="Por favor, insira apenas números válidos.", text_color="red")

# Criação da Janela
Janela = ctk.CTk()
Janela.geometry('640x400')
Janela.title("Calculadora de Viagem")

# --- Objetos internos ---

titulo = ctk.CTkLabel(Janela, 
                      text='APP VIAGEM',
                      text_color='cyan',
                      font=('Verdana', 45, 'bold'))
titulo.pack(pady=(20, 10))

distancia = ctk.CTkEntry(Janela,
                         width=400,
                         height=30,
                         border_color='green',
                         placeholder_text='Digite a distância percorrida (km)',
                         placeholder_text_color='green')
distancia.pack(pady=10)

consumo = ctk.CTkEntry(Janela,
                       width=400,
                       height=30,
                       border_color='green',
                       placeholder_text='Digite o consumo estimado (km/l)',
                       placeholder_text_color='green')
consumo.pack(pady=10)

preco = ctk.CTkEntry(Janela,
                     width=400,
                     height=30,
                     border_color='green',
                     placeholder_text='Digite o preço atual do combustível (R$)',
                     placeholder_text_color='green')
preco.pack(pady=10)

botao = ctk.CTkButton(Janela,
                      width=200,
                      height=40,
                      text='Calcular Gasto',
                      fg_color='green',
                      hover_color='darkgreen',
                      font=('Verdana', 14, 'bold'),
                      command=CalcularGasto)
botao.pack(pady=20) # <-- Adicionado o pack() que faltava

# Mudamos de CTkEntry para CTkLabel para poder exibir a mensagem corretamente
resultado = ctk.CTkLabel(Janela,
                         text_color= 'Yellow',
                         text='', # Começa vazio
                         font=('Verdana', 16, 'bold'))
resultado.pack(pady=10)

# Inicia o loop do App
Janela.mainloop()