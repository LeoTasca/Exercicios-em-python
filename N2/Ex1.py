import psycopg2
from psycopg2 import Error

try:
    #conectar com o database
    conexao = psycopg2.connect(
        host="localhost",
        database="prova",
        user="postgres",
        password="tasca",)

    #cursor
    cursor = conexao.cursor()
    
    #definir as colunas da tabela música
    inserir_query = '''INSERT INTO música (ID, NOME, AUTOR, GENERO) VALUES (%s,%s,%s,%s)'''

    #definir os registros
    inserir_registro_1 = (1, 'Bohemian Rhapsody', 'Queen', 'Rock')
    inserir_registro_2 = (2, 'Dreams', 'Fleetwood Mac', 'Rock')

    #inserir os registros na tabela
    cursor.execute(inserir_query, inserir_registro_1)
    cursor.execute(inserir_query, inserir_registro_2)

    #comitar os registros no database
    conexao.commit()
    print("\nRegistro inserido com sucesso na tabela música\n")

#exceção para se ocorrer um erro ao inserir os registros na tabela
except (Exception, psycopg2.Error) as error:
    if(conexao):
        print("\nFalha ao inserir o registro na tabela música\n", error)

#se tudo ocorrer corretamente, a conexão com o database é encerrada
finally:
    if(conexao):
        cursor.close()
        conexao.close()
        print("A conexão com PostgreSQL foi encerrada\n")