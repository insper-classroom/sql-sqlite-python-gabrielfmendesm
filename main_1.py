import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Estudantes")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoDeIngresso INTEGER
);
""")
               
estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, AnoDeIngresso)
VALUES (?, ?, ?);
""", estudantes)

conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print("Todos os estudantes:")
print(cursor.fetchall())

# Exibir todos os estudantes que ingressaram entre 2019 e 2020
cursor.execute("SELECT * FROM Estudantes WHERE AnoDeIngresso BETWEEN 2019 AND 2020")
print('\n')
print("Estudantes que ingressaram entre 2019 e 2020:")
print(cursor.fetchall())

# Atualizar o ano de ingresso para 2054 de um estudante específico
estudante = 'Ana Silva'
cursor.execute("UPDATE Estudantes SET AnoDeIngresso = ? WHERE Nome = ?", (2054, estudante))
conn.commit()

# Exibir todos os estudantes após a atualização
cursor.execute("SELECT * FROM Estudantes")
print('\n')
print("Após a atualização (1):")
print(cursor.fetchall())

id_estudante = 2
# Excluir o registro com o ID especificado
cursor.execute("DELETE FROM Estudantes WHERE ID = ?", (id_estudante,))
conn.commit()

# Exibir todos os estudantes após a atualização
cursor.execute("SELECT * FROM Estudantes")
print('\n')
print("Após a atualização (2):")
print(cursor.fetchall())

# Exibir todos os estudantes de computação que ingressaram após 2019
cursor.execute("SELECT * FROM Estudantes WHERE Curso = 'Computação' AND AnoDeIngresso > 2019")
print('\n')
print("Estudantes de computação que ingressaram após 2019:")
print(cursor.fetchall())

# Alterar todos os anos de ingresso para 2018 apenas dos alunos de computação
cursor.execute("UPDATE Estudantes SET AnoDeIngresso = 2018 WHERE Curso = 'Computação'")
conn.commit()

# Exibir todos os estudantes após a atualização
cursor.execute("SELECT * FROM Estudantes")
print('\n')
print("Após a atualização (3):")
print(cursor.fetchall())

# Fechar a conexão com o banco de dados
conn.close()