from db import get_connection
import customtkinter as ctk
from gui_cadastro_envio import abrir_tela_cadastro_envio
from gui_consultas import abrir_tela_consulta
from gui_atualizar_status import abrir_tela_atualizar_status
from gui_gerenciar_usuarios import abrir_tela_gerenciar_usuarios
from gui_auditoria import abrir_tela_auditoria
from gui_gerenciar_envios import abrir_tela_gerenciar_envios

def abrir_tela_principal(user):
    janela = ctk.CTk()
    janela.title(f"Bem-vindo, {user['login']}!")
    janela.geometry("800x400")

    tipo = user["tipo"]

    titulo = ctk.CTkLabel(janela, text=f"Você está logado como: {tipo.upper()}", font=("Arial",22,"bold"))
    titulo.pack(pady=20)

    # ------- TIPO USUÁRIO -------
    if tipo == "usuario":
        ctk.CTkLabel(janela, text="Funções básicas disponíveis.").pack(pady=10)
        ctk.CTkButton(janela, text="Consultar Envio", command=abrir_tela_consulta).pack(pady=10)

    # ------- TIPO OPERADOR -------
    elif tipo == "operador":
        ctk.CTkButton(janela, text="Registrar Envio", command=abrir_tela_cadastro_envio).pack(pady=10)
        ctk.CTkButton(janela, text="Atualizar Status", command=abrir_tela_atualizar_status).pack(pady=10)
        ctk.CTkButton(janela, text="Consultar Envio", command=abrir_tela_consulta).pack(pady=10)

    # ------- TIPO ADMIN -------
    elif tipo == "admin":
        ctk.CTkButton(janela, text="Gerenciar Usuários", command=abrir_tela_gerenciar_usuarios).pack(pady=10)
        ctk.CTkButton(janela, text="Visualizar Auditoria", command=abrir_tela_auditoria).pack(pady=10)
        ctk.CTkButton(janela, text="Gerenciar Envios", command=abrir_tela_gerenciar_envios).pack(pady=10)
        ctk.CTkButton(janela, text="Consultar Envio", command=abrir_tela_consulta).pack(pady=10)

    janela.mainloop()
