import mysql.connector # type: ignore
from mysql.connector import Error # type: ignore
import time
import getpass
import random
import bcrypt
import uuid

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host = 'localhost',
            database = 'db_logistica',
            user = 'root',
            password = '',
        )
        if conexao.is_connected():
            print("Conexão realizada com sucesso!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao mysql: {e}")
        return None
        
def login():
    print("\n===== LOGIN =====")
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    conn = conectar_banco()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tb_users WHERE login = %s", (usuario,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        print("Usuário não encontrado!\n")
        return None

    if not bcrypt.checkpw(senha.encode(), user["senha"].encode()):
        print("Senha incorreta!\n")
        return None

    cargo = user["tipo"].lower()

    if cargo not in ("admin", "operador"):
        print(f"Acesso negado! Usuário do tipo '{cargo}' não tem permissão.\n")
        return None

    print(f"Login realizado com sucesso! Bem-vindo, {usuario} ({cargo}).\n")
    return user

def atualizar_status():
    print("\n--- Atualizar status de envio ---")
    codigo = input("Código do envio: ")

    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT condicao, localizacao FROM tb_envios WHERE codigo=%s", (codigo,))
    dados = cursor.fetchone()

    if not dados:
        print("Código não encontrado!")
        conn.close()
        return

    status_antigo, local_antiga = dados

    novo_status = input("Novo status (Pendente / Em trânsito / Entregue): ").lower()
    nova_local = input("Nova localização: ")

    cursor.execute("""
        UPDATE tb_envios 
        SET condicao=%s, localizacao=%s 
        WHERE codigo=%s
    """, (novo_status, nova_local, codigo))

    # Auditoria
    cursor.execute("""
        INSERT INTO tb_auditoria (codigo, status_antigo, status_novo, local_antigo, local_novo, data_hora)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (codigo, status_antigo, novo_status, local_antiga, nova_local, time.ctime()))

    conn.commit()
    conn.close()

    print("Status atualizado com sucesso!")

def listar_por_status():
    print("\n--- Listar envios por status ---")
    status = input("Informe o status (pendente / em trânsito / entregue): ").lower()

    conn = conectar_banco()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT codigo, descricao, condicao, localizacao,
               remetente, destinatario, end_remetente,
               end_destinatario, data_postagem
        FROM tb_envios 
        WHERE condicao = %s
    """, (status, ))

    linhas = cursor.fetchall()
    conn.close()

    if not linhas:
        print("Nenhum envio encontrado com esse status.")
        return

    print(f"\nEnvios com status '{status}':")
    for row in linhas:
        print("\n-------------------------------")
        print(f"Código:                {row['codigo']}")
        print(f"Descrição:             {row['descricao']}")
        print(f"Status:                {row['condicao']}")
        print(f"Localização:           {row['localizacao']}")
        print(f"Remetente:             {row['remetente']}")
        print(f"Destinatário:          {row['destinatario']}")
        print(f"End. Remetente:        {row['end_remetente']}")
        print(f"End. Destinatário:     {row['end_destinatario']}")
        print(f"Data/hora Postagem:    {row['data_postagem']}")
        print("-------------------------------")

def historico():
    print("\n--- Histórico de alterações ---")
    codigo = input("Informe o código do envio: ")

    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status_antigo, status_novo, local_antigo, local_novo, data_hora
        FROM tb_auditoria
        WHERE codigo=%s
        ORDER BY id_auditoria ASC
    """, (codigo,))

    registros = cursor.fetchall()
    conn.close()

    if not registros:
        print("Nenhum histórico encontrado.")
        return

    print(f"\nHistórico do envio {codigo}:")
    for a, b, c, d, hora in registros:
        print(f"[{hora}] | Local: {c} -> {d} | Status: {a} -> {b}")
        
def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Atualizar status/localização")
        print("2 - Listar envios por status")
        print("3 - Histórico por código")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            atualizar_status()
        elif op == "2":
            listar_por_status()
        elif op == "3":
            historico()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    conectar_banco()
    usuario_logado = login()
    if usuario_logado:
        menu()