# gui_gerenciar_usuarios.py

import customtkinter as ctk
from tkinter import messagebox
from db import get_connection


# ============================
# FUNÇÃO: Deletar usuário
# ============================
def excluir_usuario(id_user, frame_lista):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tb_users WHERE id_user = %s", (id_user,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Usuário removido!")
    carregar_usuarios(frame_lista)  # <-- Atualiza a lista na hora


# ============================
# FUNÇÃO: Carregar lista de usuários
# ============================
def carregar_usuarios(frame_lista):
    # Limpa GUI
    for widget in frame_lista.winfo_children():
        widget.destroy()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id_user, login, tipo FROM tb_users")
    usuarios = cursor.fetchall()
    conn.close()

    # Cabeçalho
    ctk.CTkLabel(frame_lista, text="ID", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=5, pady=5)
    ctk.CTkLabel(frame_lista, text="Usuário", font=("Arial", 14, "bold")).grid(row=0, column=1, padx=5, pady=5)
    ctk.CTkLabel(frame_lista, text="Tipo", font=("Arial", 14, "bold")).grid(row=0, column=2, padx=5, pady=5)
    ctk.CTkLabel(frame_lista, text="Ações", font=("Arial", 14, "bold")).grid(row=0, column=3, padx=5, pady=5)

    # Lista
    for i, user in enumerate(usuarios, start=1):
        ctk.CTkLabel(frame_lista, text=user["id_user"]).grid(row=i, column=0, padx=5, pady=5)
        ctk.CTkLabel(frame_lista, text=user["login"]).grid(row=i, column=1, padx=5, pady=5)
        ctk.CTkLabel(frame_lista, text=user["tipo"]).grid(row=i, column=2, padx=5, pady=5)

        # Botão Excluir (AGORA SEM ERRO)
        ctk.CTkButton(
            frame_lista,
            text="Excluir",
            fg_color="red",
            hover_color="#aa0000",
            command=lambda uid=user["id_user"], fr=frame_lista: excluir_usuario(uid, fr)
        ).grid(row=i, column=3, padx=5)


# ============================
# ABRIR TELA DE GERENCIAMENTO
# ============================
def abrir_tela_gerenciar_usuarios():
    janela = ctk.CTkToplevel()
    janela.title("Gerenciar Usuários")
    janela.geometry("600x500")

    ctk.CTkLabel(janela, text="Gerenciamento de Usuários", font=("Arial", 22, "bold"))\
        .pack(pady=20)

    frame_lista = ctk.CTkFrame(janela)
    frame_lista.pack(pady=10, fill="both", expand=True)

    carregar_usuarios(frame_lista)
