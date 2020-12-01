import psycopg2
from N3.conexao import Conexao

class Aluno():

    def cadastrar(self, nome, matricula):
        try:
            conexao = Conexao().conexaoDatabase()
            cursor = conexao.cursor()
            #cadastrar os registros na tabela
            cadastrar = f"Inserir into aluno (nome, matricula) values ('{nome}', '{matricula}');"
            cursor.execute(cadastrar)
            #comitar os registros no database
            conexao.commit()
            return f"Aluno {nome}({matricula}) foi cadastrado com sucesso no banco de dados"
        #exceção para se ocorrer um erro ao cadastrar os registros na tabela
        except (Exception, psycopg2.DatabaseError) as error:
            print("\nFalha ao cadastrar o registro\n", error)
        #se tudo ocorrer corretamente, a conexão com o database é encerrada
        finally:
            if conexao:
                cursor.close()
                conexao.close()
                print("A conexão com PostgreSQL foi encerrada\n")

    def consultar(self):
        try:
            conexao = Conexao().conexaoDatabase()
            cursor = conexao.cursor()
            select = f"SELECT * FROM aluno;"
            cursor.execute(select)
            aluno = cursor.fetchall()

            if len(aluno):
                return aluno
            else:
                return "Nenhum registro foi encontrado"

        except (Exception, psycopg2.Error) as error:
            print("\nFalha ao consultar o registro\n", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()
                print("A conexão com PostgreSQL foi encerrada\n")

    def editar(self, matricula):
        try:
            conexao = Conexao().conexaoDatabase()
            cursor = conexao.cursor()
            editar = f"UPDATE aluno WHERE matricula='{matricula}"
            cursor.execute(editar)
            conexao.commit()
            return f"O aluno com a matricula={matricula} teve seus dados atualizados"

        except (Exception, psycopg2.Error) as error:
            print("\nFalha ao atualizar o registro\n", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()

    def remover(self, matricula):
        try:
            conexao = Conexao().conexaoDatabase()
            cursor = conexao.cursor()
            remover = f"DELETE from aluno WHERE matricula='{matricula}';"
            cursor.execute(remover)
            conexao.commit()
            return f"O aluno com a matricula={matricula} foi removido"

        except (Exception, psycopg2.Error) as error:
            print("\nFalha ao remover o registro\n", error)

        finally:
            if (conexao):
                cursor.close()
                conexao.close()
                print("A conexão com PostgreSQL foi encerrada\n")