from db import get_connection
import customtkinter as ctk

def abrir_tela_principal(user):
    janela = ctk.CTk()
    janela.title(f"Bem-vindo, {user['login']}!")
    janela.geometry("800x400")

    tipo = user["tipo"]

    titulo = ctk.CTkLabel(janela, text=f"Você está logado como: {tipo.upper()}", font=("Arial",22,"bold"))
    titulo.pack(pady=20)

    # Telas para cada tipo
    if tipo == "usuario":
        bot = ctk.CTkLabel(janela, text="Funções básicas disponíveis.")
        bot.pack(pady=10)

    elif tipo == "operador":
        bot = ctk.CTkButton(janela, text="Registrar Envio")
        bot.pack(pady=10)

        bot2 = ctk.CTkButton(janela, text="Atualizar Status")
        bot2.pack(pady=10)

    elif tipo == "admin":
        adm1 = ctk.CTkButton(janela, text="Gerenciar Usuários")
        adm1.pack(pady=10)

        adm2 = ctk.CTkButton(janela, text="Visualizar Auditoria")
        adm2.pack(pady=10)

        adm3 = ctk.CTkButton(janela, text="Gerenciar Envios")
        adm3.pack(pady=10)

    janela.mainloop()
