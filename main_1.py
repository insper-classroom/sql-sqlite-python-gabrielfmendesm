import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
# A função connect() estabelece uma conexão com o banco de dados SQLite e retorna um objeto de conexão.
conn = sqlite3.connect('db/database_alunos.db')

# Um cursor é um objeto que permite interagir com o banco de dados, 
# como executar instruções SQL e recuperar dados.
cursor = conn.cursor()

# Exclui a tabela Estudantes se existir (mais facíl na hora rodar o programa sem adicionar registros repetidos)
cursor.execute("DROP TABLE IF EXISTS Estudantes")
conn.commit()

# Criar tabela de Estudantes
# Usamos o método execute() do cursor para executar instruções SQL.
# Neste caso, estamos criando uma tabela chamada Estudantes.
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoDeIngresso INTEGER
);
""")

# Inserir registros de Estudantes
# Preparamos uma lista de tuplas contendo os dados dos estudantes que queremos inserir.
estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

# Usamos o método executemany() para inserir vários registros de uma vez.
# Ele toma uma consulta SQL e uma lista de tuplas como parâmetros.
cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, AnoDeIngresso)
VALUES (?, ?, ?);
""", estudantes)

# Depois de fazer alterações no banco de dados, como inserir registros,
# precisamos confirmar essas alterações usando o método commit() do objeto de conexão.
conn.commit()

# Selecione e mostre todos os registros de estudantes
# Usamos o método execute() para executar uma consulta SELECT.
cursor.execute("SELECT * FROM Estudantes")
print("Todos os estudantes:")

# O método fetchall() recupera todos os registros resultantes da consulta.
print(cursor.fetchall())

# Exibir todos os estudantes que ingressaram entre 2019 e 2020
cursor.execute("SELECT * FROM Estudantes WHERE AnoDeIngresso BETWEEN 2019 AND 2020")
print('\n')
print("Estudantes que ingressaram entre 2019 e 2020:")
print(cursor.fetchall())

# Atualizar o ano de ingresso para 2054 de um estudante específico
cursor.execute("UPDATE Estudantes SET AnoDeIngresso = ? WHERE ID = ?", (2054, 1))
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