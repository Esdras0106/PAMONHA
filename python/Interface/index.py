import customtkinter as ctk
import webbrowser
import os

# O padx no CustomTkinter é o parâmetro responsável pelo espaçamento horizontal externo.
# O pady no CustomTkinter é o parâmetro responsável pelo espaçamento vertical externo.

#----- Funções dos botões -----#
def desligar():
    os.system("shutdown /s /t 0")

def reiniciar():
    os.system("shutdown /r /t 1")

def bloqueio():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def calculadora():
    os.system("calc")

def google():
    webbrowser.open("https://www.google.com")
    
def telaazul():
    janela2 = ctk.CTkToplevel()
    janela2.attributes("-fullscreen", True)
    janela2.configure(fg_color='#0078d7')
    
    mesnsagem = """
                :(
                Seu dispositivo encontrou um problema e precisa ser reiniciado.
                Estamos apenas coletando algumas informações de erro e, em seguida, reiniciaremos para você.

                0% concluído

                Para obter mais informações sobre esse problema e possíveis correções, visite:
                https://www.windows.com/stopcode

                Código de parada: CRITICAL_PROCESS_DIED
                """
        
    texto = ctk.CTkLabel(janela2,
                        text=mesnsagem,
                        font=('Arial',32),
                        justify="left",
                        text_color="white")
    texto.pack(expand=True)

ctk.set_appearance_mode("light")

#----- Configurações da janela -----#
janela = ctk.CTk()
janela.geometry("350x400")
janela.title("Bomba Patch 2026")

label = ctk.CTkLabel(janela,
                    text="Bem-vindo ao Bomba Patch 2026!",
                    font=ctk.CTkFont(size=20, weight="bold"))
label.pack(pady=20)

btndesligar = ctk.CTkButton(janela,
                            text="Desligar",
                            command=desligar,
                            width=150,
                            height=30,
                            fg_color="black",
                            hover_color="#686868").pack(pady=10)

btnreiniciar = ctk.CTkButton(janela,
                            text="Reiniciar",
                            command=reiniciar,
                            width=150,
                            height=30,
                            fg_color="black",
                            hover_color="#686868").pack(pady=10)

btnbloqueio = ctk.CTkButton(janela,
                            text="Bloquear",
                            command=bloqueio,
                            width=150,
                            height=30,
                            fg_color="black",
                            hover_color="#686868").pack(pady=10)

btncalculadora = ctk.CTkButton(janela,
                               text="Calculadora",
                               command=calculadora,
                               width=150,
                               height=30,
                               fg_color="black",
                               hover_color="#686868").pack(pady=10)

btngoogle = ctk.CTkButton(janela,
                          text="Google",
                          command=google,
                          width=150,
                          height=30,
                          fg_color="black",
                          hover_color="#686868").pack(pady=10)

btntelaazul = ctk.CTkButton(janela,
                            text="NÃO CLIQUE AQUI!",
                            command=telaazul,
                            width=250,
                            height=40,
                            fg_color="red",
                            hover_color="#ff3247").pack(pady=10)

janela.mainloop()