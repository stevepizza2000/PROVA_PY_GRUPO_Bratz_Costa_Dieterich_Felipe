import bcrypt
from db import get_connection

def criar_usuario(login, senha, tipo="usuario"):
    conn = get_connection()
    cursor = conn.cursor()

    # Gera o hash da senha e DECODIFICA ele, não a senha original
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

    cursor.execute("""
        INSERT INTO tb_users (login, senha, tipo)
        VALUES (%s, %s, %s)
    """, (login, senha_hash, tipo))

    conn.commit()
    conn.close()


def autenticar(login, senha):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tb_users WHERE login = %s", (login,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return None

    # Comparar a senha digitada com o hash salvo
    if bcrypt.checkpw(senha.encode(), user["senha"].encode()):
        return user

    return None

