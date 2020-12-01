import psycopg2

class Conexao():
#conectar com o database
  def conexaoDatabase(self):
    conexao = psycopg2.connect(
      host="localhost",
      database="prova",
      user="postgres",
      password="tasca",)

    return conexao
