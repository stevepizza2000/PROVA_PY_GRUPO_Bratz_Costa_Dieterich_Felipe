import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_logistica"
    )

def registrar_auditoria(codigo, status_antigo, status_novo, local_antigo, local_novo):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tb_auditoria 
        (codigo, status_antigo, status_novo, local_antigo, local_novo, data_hora)
        VALUES (%s, %s, %s, %s, %s, NOW())
    """, (codigo, status_antigo, status_novo, local_antigo, local_novo))

    conn.commit()
    conn.close()