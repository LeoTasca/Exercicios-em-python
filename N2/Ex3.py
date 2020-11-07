from pymongo import MongoClient

#conectar com o database, indicando host e porta
cliente = MongoClient('localhost', 27017)

#seleciona o banco 'prova'
banco = cliente.prova

#seleciona a coleção 'música'
musica = banco.música

#inserir mais de um documento
música = [
    {
        "nome": "Bohemian Rhapsody",
        "autor": "Queen",
        "genero": "Rock"
    },
    {
        "nome": "Dreams",
        "autor": "Fleetwood Mac",
        "genero": "Rock"
    }
]

#comitar os documentos na coleção
musica.insert_many(música)
print("\nDocumento inserido com sucesso na coleção música\n")