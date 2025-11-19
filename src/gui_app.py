import customtkinter as ctk
from auth import criar_usuario
from gui_app2 import abrir_tela_login

ctk.set_appearance_mode("dark")

def abrir_tela_cadastro():
    janela = ctk.CTk()
    janela.title("Cadastro")
    janela.geometry("800x450")

    titulo = ctk.CTkLabel(janela, text="Cadastro de Usuário", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)

    # -------- Usuário --------
    frame1 = ctk.CTkFrame(janela)
    frame1.pack(pady=10)

    ctk.CTkLabel(frame1, text="Usuário:", font=("Arial", 12, "bold")).pack(side="left", padx=15)
    user = ctk.CTkEntry(frame1, placeholder_text="Digite seu usuário")
    user.pack(side="left")

    # -------- Senha --------
    frame2 = ctk.CTkFrame(janela)
    frame2.pack(pady=10)

    ctk.CTkLabel(frame2, text="Senha:", font=("Arial", 12, "bold")).pack(side="left", padx=15)
    senha = ctk.CTkEntry(frame2, placeholder_text="Digite sua senha", show="*")
    senha.pack(side="left")

    # -------- Tipo de conta --------
    frame3 = ctk.CTkFrame(janela)
    frame3.pack(pady=10)

    ctk.CTkLabel(frame3, text="Tipo:", font=("Arial", 12, "bold")).pack(side="left", padx=15)

    tipos = ["usuario", "operador", "admin"]
    tipo_selecionado = ctk.CTkOptionMenu(frame3, values=tipos)
    tipo_selecionado.pack(side="left")

    # -------- Função cadastrar --------
    def cadastrar():
        login = user.get()
        password = senha.get()
        tipo = tipo_selecionado.get()

        criar_usuario(login, password, tipo)
        print(f"Usuário {login} cadastrado como {tipo}!")

        janela.destroy()
        abrir_tela_login()

    ctk.CTkButton(janela, text="Cadastrar", command=cadastrar).pack(pady=20)

    # -------- Botão IR PARA LOGIN --------
    def ir_para_login():
        janela.destroy()
        abrir_tela_login()

    ctk.CTkButton(
        janela,
        text="Já tenho uma conta (Login)",
        command=ir_para_login
    ).pack(pady=10)

    janela.mainloop()


# Executa a tela caso seja aberto diretamente
if __name__ == "__main__":
    abrir_tela_cadastro()
