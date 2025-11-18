import customtkinter as ctk

# Aparência
ctk.set_appearance_mode("dark")

janela = ctk.CTk()
janela.title("Login")
janela.geometry("800x400")

titulo = ctk.CTkLabel(janela, text="Para Prosseguir, Faça seu Cadastro!", font=("Arial",22,"bold"))
titulo.pack(pady=80)

frame1 = ctk.CTkFrame(janela)
frame1.pack(pady=10)

t1 = ctk.CTkLabel(frame1, text="Usuário:", font=("Arial",12,"bold"))
t1.pack(side="left", padx=15,)

user = ctk.CTkEntry(frame1, placeholder_text="Digite seu usuário")
user.pack(side="left")

frame2 = ctk.CTkFrame(janela)
frame2.pack(pady=40)

t2 = ctk.CTkLabel(frame2, text="Senha:", font=("Arial",12,"bold"))
t2.pack(side="left", padx=15)

senha = ctk.CTkEntry(frame2, placeholder_text="Digite sua senha")
senha.pack(side="left")

b = ctk.CTkButton(janela, text="Cadastrar")
b.pack(pady=20)




janela.mainloop()