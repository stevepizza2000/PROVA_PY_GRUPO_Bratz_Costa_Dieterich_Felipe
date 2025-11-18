import os
import time
import subprocess
import webbrowser

print("=== Instalador Universal ===\n")
print("1 - Instalar GUI")
print("2 - Instalar CLI")
print("3 - Instalar WEB\n")

op = input("Escolha: ")

# Diretorio base do projeto
base = os.path.dirname(os.path.abspath(__file__))
build = os.path.join(base, "build")
src = os.path.join(base, "src")

def run_executable(path):
    if os.path.exists(path):
        print(f"Executando: {path}")
        subprocess.Popen(path)
    else:
        print("Erro: arquivo não encontrado:", path)

if op == "1":
    gui_exe = os.path.join(build, "gui_executable.exe")
    print("Iniciando instalação GUI...")
    time.sleep(1)
    run_executable(gui_exe)

elif op == "2":
    cli_exe = os.path.join(build, "cli_executable.exe")
    print("Iniciando instalação CLI...")
    time.sleep(1)
    run_executable(cli_exe)

elif op == "3":
    print("Iniciando WEB...\n")
    time.sleep(1)

    # Forma A: abrir executável web
    web_exe = os.path.join(build, "web_executable.exe")

    if os.path.exists(web_exe):
        run_executable(web_exe)
    else:
        # Forma B: rodar app web em Python
        web_app = os.path.join(src, "web_app.py")
        print("Executando web_app.py...")
        subprocess.Popen(["python", web_app])
        time.sleep(2)
        webbrowser.open("http://127.0.0.1:5000")

else:
    print("Opção inválida!")
