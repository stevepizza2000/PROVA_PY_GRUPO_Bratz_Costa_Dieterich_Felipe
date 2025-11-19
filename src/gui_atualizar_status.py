# gui_atualizar_status.py

import customtkinter as ctk
from tkinter import messagebox
from db import get_connection


def atualizar_status_no_banco(codigo, novo_status, nova_localizacao):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # 1 — Buscar registros atuais
    cursor.execute("SELECT condicao, localizacao FROM tb_envios WHERE codigo = %s", (codigo,))
    envio = cursor.fetchone()

    if envio is None:
        conn.close()
        return False

    status_antigo = envio["condicao"]
    local_antigo = envio["localizacao"]

    # 2 — Atualizar tabela tb_envios
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tb_envios
        SET condicao = %s, localizacao = %s
        WHERE codigo = %s
    """, (novo_status, nova_localizacao, codigo))

    # 3 — Registrar na AUDITORIA
    cursor.execute("""
        INSERT INTO tb_auditoria (codigo, status_antigo, status_novo, local_antigo, local_novo)
        VALUES (%s, %s, %s, %s, %s)
    """, (codigo, status_antigo, novo_status, local_antigo, nova_localizacao))

    conn.commit()
    conn.close()
    return True


def abrir_tela_atualizar_status():
    janela = ctk.CTkToplevel()
    janela.title("Atualizar Status de Envio")
    janela.geometry("500x450")
    janela.resizable(False, False)

    ctk.CTkLabel(janela, text="Atualizar Status", font=("Arial", 24, "bold")).pack(pady=20)

    frame = ctk.CTkFrame(janela)
    frame.pack(pady=10)

    # ---- CÓDIGO ----
    ctk.CTkLabel(frame, text="Código de Rastreamento:").grid(row=0, column=0, padx=10, pady=10)
    entry_codigo = ctk.CTkEntry(frame, width=250)
    entry_codigo.grid(row=0, column=1, pady=10)

    # ---- STATUS (MATCH ENUM DO BANCO) ----
    ctk.CTkLabel(frame, text="Novo Status:").grid(row=1, column=0, padx=10, pady=10)

    status_opcoes = ["pendente", "em trânsito", "entregue"]   # 🔥 Correto!
    entry_status = ctk.CTkOptionMenu(frame, values=status_opcoes, width=250)
    entry_status.grid(row=1, column=1, pady=10)

    # ---- LOCALIZAÇÃO ----
    ctk.CTkLabel(frame, text="Nova Localização:").grid(row=2, column=0, padx=10, pady=10)
    entry_localizacao = ctk.CTkEntry(frame, width=250)
    entry_localizacao.grid(row=2, column=1, pady=10)

    def salvar():
        codigo = entry_codigo.get()
        novo_status = entry_status.get()
        nova_localizacao = entry_localizacao.get()

        if not codigo or not nova_localizacao:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        sucesso = atualizar_status_no_banco(codigo, novo_status, nova_localizacao)

        if sucesso:
            messagebox.showinfo("Sucesso", "Status atualizado com sucesso!")
            entry_codigo.delete(0, ctk.END)
            entry_localizacao.delete(0, ctk.END)
        else:
            messagebox.showerror("Erro", "Código não encontrado no banco.")

    ctk.CTkButton(janela, text="Salvar Alterações", width=200, height=40, command=salvar).pack(pady=20)
