from db.db_utils import *

# Conexão com o banco de dados dentro da pasta "db"
conn = conectar_banco_dados('db/database_alunos2.db')

# Criar tabela de Estudantes (exclui a tabela Estudantes se existir)
criar_tabela(conn, 'Estudantes')

# Inserir registros de Estudantes
estudantes = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

adicionar_registros(conn, 'Estudantes', estudantes)

# Mostrar todos os registros de estudantes
mostrar_registros(conn, 'Estudantes')

# Mostrar todos os estudantes que ingressaram entre 2019 e 2020
mostrar_registros_por_ano(conn, 'Estudantes', 2019, 2020)

# Atualizar o ano de ingresso de um estudante específico
atualizar_registro(conn, 'Estudantes', 1, 2054)

# Mostrar todos os estudantes após a atualização
mostrar_registros(conn, 'Estudantes')

# Excluir o registro com o ID especificado
excluir_registro(conn, 'Estudantes', 2)

# Mostrar todos os estudantes após a atualização
mostrar_registros(conn, 'Estudantes')

# Mostrar todos os estudantes de computação que ingressaram após 2019
mostrar_registros_apos_ano(conn, 'Estudantes', 'Computação', 2019)

# Alterar o ano de ingresso de todos os estudantes de computação para 2018
alterar_ano_de_ingresso(conn, 'Estudantes', 'Computação', 2018)

# Mostrar todos os estudantes após a atualização
mostrar_registros(conn, 'Estudantes')

# Fechar a conexão com o banco de dados
fechar_conexao(conn)