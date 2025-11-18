from db import get_connection
import customtkinter as ctk
from auth import autenticar
from gui_app3 import abrir_tela_principal

def abrir_tela_login():
    login_win = ctk.CTk()
    login_win.title("Login")
    login_win.geometry("800x400")

    lbl = ctk.CTkLabel(login_win, text="Faça seu Login", font=("Arial",22,"bold"))
    lbl.pack(pady=40)

    f1 = ctk.CTkFrame(login_win)
    f1.pack(pady=10)

    ctk.CTkLabel(f1, text="Usuário:").pack(side="left", padx=10)
    login_entry = ctk.CTkEntry(f1)
    login_entry.pack(side="left")

    f2 = ctk.CTkFrame(login_win)
    f2.pack(pady=10)

    ctk.CTkLabel(f2, text="Senha:").pack(side="left", padx=10)
    senha_entry = ctk.CTkEntry(f2, show="*")
    senha_entry.pack(side="left")

    def tentar_login():
        user = autenticar(login_entry.get(), senha_entry.get())

        if user:
            print("Login feito com sucesso!")
            login_win.destroy()
            abrir_tela_principal(user)   
        else:
            print("Login inválido!")

    botao = ctk.CTkButton(login_win, text="Entrar", command=tentar_login)
    botao.pack(pady=20)

    login_win.mainloop()