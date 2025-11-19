# gui_gerenciar_envios.py

import customtkinter as ctk
from tkinter import messagebox
from db import get_connection


def carregar_envios(frame_lista):
    for widget in frame_lista.winfo_children():
        widget.destroy()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tb_envios")
    envios = cursor.fetchall()
    conn.close()

    for i, envio in enumerate(envios):
        ctk.CTkLabel(frame_lista, text=envio["codigo"]).grid(row=i, column=0, padx=5)
        ctk.CTkLabel(frame_lista, text=envio["descricao"]).grid(row=i, column=1, padx=5)
        ctk.CTkLabel(frame_lista, text=envio["condicao"]).grid(row=i, column=2, padx=5)

        ctk.CTkButton(
            frame_lista, text="Editar",
            command=lambda e=envio: abrir_editor_envio(e)
        ).grid(row=i, column=3, padx=5)

        ctk.CTkButton(
            frame_lista, text="Excluir",
            command=lambda codigo=envio["codigo"]: excluir_envio(codigo, frame_lista)
        ).grid(row=i, column=4, padx=5)


def excluir_envio(codigo, frame_lista):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tb_envios WHERE codigo = %s", (codigo,))
    conn.commit()
    conn.close()

    messagebox.showinfo("OK", "Envio removido!")
    carregar_envios(frame_lista)


def salvar_auditoria(codigo, antigo_s, novo_s, antigo_l, novo_l):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_auditoria (codigo, status_antigo, status_novo, local_antigo, local_novo, data_hora)
        VALUES (%s, %s, %s, %s, %s, NOW())
    """, (codigo, antigo_s, novo_s, antigo_l, novo_l))

    conn.commit()
    conn.close()


def abrir_editor_envio(envio):
    janela = ctk.CTkToplevel()
    janela.title("Editar Envio")
    janela.geometry("500x600")

    ctk.CTkLabel(janela, text=f"Editar Envio {envio['codigo']}", font=("Arial", 20, "bold")).pack(pady=10)

    # Campos
    campos = [
        "descricao", "condicao", "localizacao",
        "remetente", "destinatario",
        "end_remetente", "end_destinatario",
        "data_postagem",
    ]

    entries = {}

    frame = ctk.CTkFrame(janela)
    frame.pack(pady=10)

    for i, camp in enumerate(campos):
        ctk.CTkLabel(frame, text=camp).grid(row=i, column=0, padx=5, pady=5)
        ent = ctk.CTkEntry(frame, width=250)
        ent.insert(0, envio[camp])
        ent.grid(row=i, column=1, pady=5)
        entries[camp] = ent

    def salvar():
        dados_novos = {c: entries[c].get() for c in campos}

        antigo_status = envio["condicao"]
        novo_status = dados_novos["condicao"]

        antigo_local = envio["localizacao"]
        novo_local = dados_novos["localizacao"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tb_envios 
            SET descricao=%s, condicao=%s, localizacao=%s,
                remetente=%s, destinatario=%s,
                end_remetente=%s, end_destinatario=%s, data_postagem=%s
            WHERE codigo=%s
        """, (
            dados_novos["descricao"], dados_novos["condicao"], dados_novos["localizacao"],
            dados_novos["remetente"], dados_novos["destinatario"],
            dados_novos["end_remetente"], dados_novos["end_destinatario"],
            dados_novos["data_postagem"], envio["codigo"]
        ))

        conn.commit()
        conn.close()

        # AUDITORIA
        salvar_auditoria(
            envio["codigo"],
            antigo_status, novo_status,
            antigo_local, novo_local
        )

        messagebox.showinfo("OK", "Alterações salvas e auditadas!")

    ctk.CTkButton(janela, text="Salvar Alterações", command=salvar).pack(pady=20)


def abrir_tela_gerenciar_envios():
    janela = ctk.CTkToplevel()
    janela.title("Gerenciar Envios")
    janela.geometry("700x700")

    ctk.CTkLabel(janela, text="Gerenciamento de Envios", font=("Arial", 24, "bold")).pack(pady=20)

    frame_lista = ctk.CTkScrollableFrame(janela, width=650, height=550)
    frame_lista.pack(pady=20)

    carregar_envios(frame_lista)
