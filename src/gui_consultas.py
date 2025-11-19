import customtkinter as ctk
from tkinter import messagebox
from db import get_connection


def consultar_envio(codigo, frame_resultado):
    if not codigo:
        messagebox.showwarning("Atenção", "Informe um código de rastreio.")
        return

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tb_envios WHERE codigo = %s", (codigo,))
    envio = cursor.fetchone()

    conn.close()

    for widget in frame_resultado.winfo_children():
        widget.destroy()

    if envio is None:
        messagebox.showinfo("Não encontrado", "Nenhum envio com este código.")
        return

    for i, (campo, valor) in enumerate(envio.items()):
        ctk.CTkLabel(frame_resultado, text=f"{campo}:", font=("Arial", 14, "bold")).grid(
            row=i, column=0, sticky="w", padx=10, pady=5
        )

        ctk.CTkLabel(frame_resultado, text=str(valor), font=("Arial", 14)).grid(
            row=i, column=1, sticky="w", padx=10, pady=5
        )


def abrir_tela_consulta():
    janela = ctk.CTkToplevel()
    janela.title("Consulta de Envio")
    janela.geometry("600x650")
    janela.resizable(False, False)

    ctk.CTkLabel(janela, text="Consulta de Envio", font=("Arial", 24, "bold")).pack(pady=15)

    frame_busca = ctk.CTkFrame(janela)
    frame_busca.pack(pady=10)

    ctk.CTkLabel(frame_busca, text="Código de Rastreamento:", font=("Arial", 14)).grid(
        row=0, column=0, padx=10, pady=10
    )

    entry_codigo = ctk.CTkEntry(frame_busca, width=280)
    entry_codigo.grid(row=0, column=1, padx=10, pady=10)

    # ➤ AQUI ATIVAMOS O ENTER
    entry_codigo.bind("<Return>", lambda event: consultar_envio(entry_codigo.get(), frame_resultado))

    frame_resultado = ctk.CTkScrollableFrame(janela, width=540, height=450)
    frame_resultado.pack(pady=20)

    ctk.CTkButton(
        janela,
        text="Buscar Envio",
        height=40,
        width=200,
        command=lambda: consultar_envio(entry_codigo.get(), frame_resultado)
    ).pack(pady=10)

