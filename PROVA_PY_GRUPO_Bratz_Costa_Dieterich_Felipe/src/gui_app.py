import customtkinter as ctk
from auth import criar_usuario
from gui_app2 import abrir_tela_login

ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.title("Cadastro")
janela.geometry("800x450")

titulo = ctk.CTkLabel(janela, text="Cadastro de Usuário", font=("Arial",22,"bold"))
titulo.pack(pady=20)

# -------- Usuário --------
frame1 = ctk.CTkFrame(janela)
frame1.pack(pady=10)

ctk.CTkLabel(frame1, text="Usuário:", font=("Arial",12,"bold")).pack(side="left", padx=15)
user = ctk.CTkEntry(frame1, placeholder_text="Digite seu usuário")
user.pack(side="left")

# -------- Senha --------
frame2 = ctk.CTkFrame(janela)
frame2.pack(pady=10)

ctk.CTkLabel(frame2, text="Senha:", font=("Arial",12,"bold")).pack(side="left", padx=15)
senha = ctk.CTkEntry(frame2, placeholder_text="Digite sua senha", show="*")
senha.pack(side="left")

# -------- Tipo de conta --------
frame3 = ctk.CTkFrame(janela)
frame3.pack(pady=10)

ctk.CTkLabel(frame3, text="Tipo:", font=("Arial",12,"bold")).pack(side="left", padx=15)

# Menu com tipos
tipos = ["usuario", "operador", "admin"]
tipo_selecionado = ctk.CTkOptionMenu(frame3, values=tipos)
tipo_selecionado.pack(side="left")


# -------- Lógica --------
def cadastrar():
    login = user.get()
    password = senha.get()
    tipo = tipo_selecionado.get()

    criar_usuario(login, password, tipo)
    print(f"Usuário {login} cadastrado como {tipo}!")

    janela.destroy()
    abrir_tela_login()


b = ctk.CTkButton(janela, text="Cadastrar", command=cadastrar)
b.pack(pady=20)

janela.mainloop()

