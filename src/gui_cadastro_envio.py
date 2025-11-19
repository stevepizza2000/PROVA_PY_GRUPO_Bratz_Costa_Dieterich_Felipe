import customtkinter as ctk
from tkinter import messagebox
import random
from db import get_connection   

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def conectar_banco():
    try:
        return get_connection()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco:\n{e}")
        return None

def gerar_codigo_unico():
    conn = conectar_banco()
    cursor = conn.cursor()

    while True:
        codigo = "".join(str(random.randint(0, 9)) for _ in range(10))

        cursor.execute("SELECT 1 FROM tb_envios WHERE codigo = %s", (codigo,))
        existe = cursor.fetchone()

        if not existe:
            conn.close()
            return codigo


def salvar_envio():
    produto = entry_produto.get()
    remetente = entry_remetente.get()
    destinatario = entry_destinatario.get()
    endereco_r = entry_endereco_r.get()
    endereco_d = entry_endereco_d.get()
    data_postagem = entry_data.get()

    if not all([produto, remetente, destinatario, endereco_r, endereco_d, data_postagem]):
        messagebox.showwarning("Atenção", "Preencha todos os campos.")
        return

    codigo = gerar_codigo_unico()
    status_inicial = "pendente"

    conn = conectar_banco()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO tb_envios 
            (codigo, descricao, condicao, localizacao, remetente, destinatario, end_remetente, end_destinatario, data_postagem)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            codigo,
            produto,
            status_inicial,
            "Centro de distribuição",
            remetente,
            destinatario,
            endereco_r,
            endereco_d,
            data_postagem
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", f"Envio cadastrado!\nCódigo: {codigo}")

        entry_produto.delete(0, ctk.END)
        entry_remetente.delete(0, ctk.END)
        entry_destinatario.delete(0, ctk.END)
        entry_endereco_r.delete(0, ctk.END)
        entry_endereco_d.delete(0, ctk.END)
        entry_data.delete(0, ctk.END)

    except Exception as e:
        conn.rollback()
        messagebox.showerror("Erro", f"Erro ao salvar no banco:\n{e}")


def abrir_tela_cadastro_envio():
    root = ctk.CTk()
    root.title("Cadastro de Envio Logístico")
    root.geometry("620x650")
    root.resizable(False, False)

    title_label = ctk.CTkLabel(root, text="Cadastro de Envio", font=("Arial", 24, "bold"))
    title_label.pack(pady=15)

    frame = ctk.CTkFrame(root)
    frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Campos
    ctk.CTkLabel(frame, text="Nome do Produto:").grid(row=0, column=0, sticky="w", pady=5)
    global entry_produto
    entry_produto = ctk.CTkEntry(frame, width=300)
    entry_produto.grid(row=0, column=1, pady=5)

    ctk.CTkLabel(frame, text="Remetente:").grid(row=1, column=0, sticky="w", pady=5)
    global entry_remetente
    entry_remetente = ctk.CTkEntry(frame, width=300)
    entry_remetente.grid(row=1, column=1, pady=5)

    ctk.CTkLabel(frame, text="Endereço Remetente:").grid(row=2, column=0, sticky="w", pady=5)
    global entry_endereco_r
    entry_endereco_r = ctk.CTkEntry(frame, width=300)
    entry_endereco_r.grid(row=2, column=1, pady=5)

    ctk.CTkLabel(frame, text="Destinatário:").grid(row=3, column=0, sticky="w", pady=5)
    global entry_destinatario
    entry_destinatario = ctk.CTkEntry(frame, width=300)
    entry_destinatario.grid(row=3, column=1, pady=5)

    ctk.CTkLabel(frame, text="Endereço Destinatário:").grid(row=4, column=0, sticky="w", pady=5)
    global entry_endereco_d
    entry_endereco_d = ctk.CTkEntry(frame, width=300)
    entry_endereco_d.grid(row=4, column=1, pady=5)

    ctk.CTkLabel(frame, text="Data de Postagem (DD/MM/AAAA):").grid(row=5, column=0, sticky="w", pady=5)
    global entry_data
    entry_data = ctk.CTkEntry(frame, width=300)
    entry_data.grid(row=5, column=1, pady=5)

    btn_salvar = ctk.CTkButton(root, text="Cadastrar Envio", font=("Arial", 16),
                            command=salvar_envio, width=250, height=45)
    btn_salvar.pack(pady=25)

    root.mainloop()
