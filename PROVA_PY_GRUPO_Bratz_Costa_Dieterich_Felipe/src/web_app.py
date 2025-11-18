import os
import subprocess
import webbrowser
import time

def start_php_server():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "provahard", "provahard"))
    os.chdir(project_dir)

    php_path = "php"  # assume que PHP está no PATH

    server_cmd = [php_path, "-S", "localhost:8000"]

    process = subprocess.Popen(server_cmd)

    print("Servidor PHP iniciado em http://localhost:8000")
    
    time.sleep(1)
    webbrowser.open("http://localhost:8000")

    process.wait()

if __name__ == "__main__":
    start_php_server()
