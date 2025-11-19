import customtkinter as ctk

ctk.set_appearance_mode("dark") 
janela = ctk.CTk()
janela.title("Menu")
janela.geometry("400x300")

titulo = ctk.CTkLabel(janela, text="Escolha sua opção", font=("Arial",25,"bold"))
titulo.pack(pady=70)

b1 = ctk.CTkButton(janela, text="Login", font=("Arial",20,"bold"))
b1.pack(pady=20,padx=40)

b2 = ctk.CTkButton(janela, text="Cadastro", font=("Arial",20,"bold"))
b2.pack(padx=40)


janela.mainloop()