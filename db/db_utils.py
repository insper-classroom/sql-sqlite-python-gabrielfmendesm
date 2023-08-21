import sqlite3

def conectar_banco_dados(nome_banco):
    conn = sqlite3.connect(nome_banco)
    return conn

def criar_tabela(conn, nome_tabela):
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {nome_tabela}")
    conn.commit()

    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Curso TEXT NOT NULL,
        AnoDeIngresso INTEGER
    );
    """)
    conn.commit()

def adicionar_registros(conn, tabela, registros):
    cursor = conn.cursor()
    cursor.executemany(f"""
    INSERT INTO {tabela} (Nome, Curso, AnoDeIngresso)
    VALUES (?, ?, ?);
    """, registros)
    conn.commit()

def mostrar_registros(conn, tabela):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabela}")
    print("Todos os estudantes:")
    print(cursor.fetchall())

def mostrar_registros_por_ano(conn, tabela, ano_inicial, ano_final):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabela} WHERE AnoDeIngresso BETWEEN {ano_inicial} AND {ano_final}")
    print('\n')
    print(f"Estudantes que ingressaram entre {ano_inicial} e {ano_final}:")
    print(cursor.fetchall())

def atualizar_registro(conn, tabela, id_registro, novo_ano):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {tabela} SET AnoDeIngresso = ? WHERE ID = ?", (novo_ano, id_registro))
    conn.commit()

def excluir_registro(conn, tabela, id_registro):
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {tabela} WHERE ID = ?", (id_registro,))
    conn.commit()

def mostrar_registros_apos_ano(conn, tabela, curso, ano):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tabela} WHERE Curso = ? AND AnoDeIngresso > ?", (curso, ano))
    print('\n')
    print(f"Estudantes do curso de {curso} que ingressaram após {ano}")
    print(cursor.fetchall())

def alterar_ano_de_ingresso(conn, tabela, curso, ano):
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {tabela} SET AnoDeIngresso = ? WHERE Curso = ?", (ano, curso))
    conn.commit()

def fechar_conexao(conn):
    conn.close()