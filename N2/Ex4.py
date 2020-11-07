from pymongo import MongoClient
cliente = MongoClient('localhost', 27017)
banco = cliente.prova
pessoas = banco.pessoa

def main():
    while(1):
        opcao = input('|----Menu----|\n|1-Cadastrar |\n|2-Editar    |\n|3-Remover   |\n|4-Consultar |\n\nEscolha uma opção: ')
        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            editar()
        elif opcao == '3':
            remover()
        elif opcao == '4':
            consultar()
        else:
            print('\n-OPÇÃO INVÁLIDA-\n')

def cadastrar():
    try:
        nome = input('\nNome: ')
        cpf = input('\nCPF: ')
        email = input('\nE-mail: ')
            
        pessoas.insert_one(
            {
                "nome": nome,
                "cpf": cpf,
                "email": email
            }
        )
        print('\n-Dado inserido com sucesso-\n')

    except Exception as e:
        print(e)

def editar():
    try:
        pesquisar_cpf = input('\nPor favor inserir um cpf para editar as informações: ')
        editar_nome = input('\nNome: ')
        editar_email = input('\nE-mail: ')

        pessoas.update_one(
            {"cpf": pesquisar_cpf},
            {
                "$set": {
                    "nome": editar_nome,
                    "email": editar_email
                }
            }
        )
        print('\n-Dados alterados com sucesso-\n')
    
    except Exception as e:
        print(e)

def remover():
    try:
        remover_cpf = input('\nPor favor inserir um cpf para remover do sistema: ')
        pessoas.delete_many({"cpf":remover_cpf})
        print('\n-Pessoa excluída com sucesso-\n')

    except Exception as e:
        print(e)

def consultar():
    try:
        opcao_consultar = input('\nOpção 1 para consultar por cpf ou opção 2 para consultar por email: ')
        if opcao_consultar == '1':
            consultar_cpf = input('\nCPF: ')
            resultado = pessoas.find({"cpf":consultar_cpf})
            for consulta in resultado:
                print(consulta)
        elif opcao_consultar == '2':
            consultar_email = input('\nE-mail: ')
            resultado = pessoas.find({"email":consultar_email})
            for consulta in resultado:
                print(consulta)
        else:
            print('\n-OPÇÃO INVÁLIDA-\n')

    except Exception as e:
        print(e)

main()
cadastrar
editar()
remover()
consultar()