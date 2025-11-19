import customtkinter as ctk
from db import get_connection

def abrir_tela_auditoria():
    janela = ctk.CTkToplevel()
    janela.title("Auditoria do Sistema")
    janela.geometry("800x600")

    ctk.CTkLabel(janela, text="Registro de Auditoria", font=("Arial", 22, "bold")).pack(pady=20)

    frame = ctk.CTkScrollableFrame(janela, width=760, height=500)
    frame.pack(pady=10)

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tb_auditoria ORDER BY data_hora DESC")
    logs = cursor.fetchall()
    conn.close()

    for i, log in enumerate(logs):
        texto = (
            f"ID: {log['id_auditoria']}\n"
            f"Código: {log['codigo']}\n"
            f"Status: {log['status_antigo']} → {log['status_novo']}\n"
            f"Localização: {log['local_antigo']} → {log['local_novo']}\n"
            f"Horário: {log['data_hora']}\n"
            "---------------------------------------------"
        )

        ctk.CTkLabel(frame, text=texto, anchor="w", justify="left").pack(pady=5)
