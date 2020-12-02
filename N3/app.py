from flask import Flask, request, jsonify
from aluno import Aluno

#indicando qua a aplicaçao vai ser flask
app = Flask(__name__)

aluno = Aluno()

#mapear o recurso
@app.route("/")
def contextoApp():
    return "Bem Vindo ao CRUD Aluno"

#post para cadastrar
@app.route(f"/alunos/cadastrar", methods=['POST'])
def cadastrarAluno():
    nome = request.args.get('nome')
    matricula = request.args.get('matricula')
    try:
        return aluno.cadastrar(nome, matricula)
    except Exception as e:
        return str(e)
    return

#get para consultar
@app.route("/alunos/consultar", methods=['GET'])
def consultarAluno():
    alunos = aluno.consultar()
    return jsonify(alunos)

#put para editar
@app.route(f"/alunos/editar", methods=['PUT'])
def editarAluno():
    nome = request.args.get('nome')
    matricula = request.args.get('matricula')
    try:
        return aluno.editar(nome, matricula)
    except Exception as e:
        return str(e)
    return

#delete para remover
@app.route(f"/alunos/remover", methods=['DELETE'])
def removerAluno():
    matricula = request.args.get('matricula')
    try:
        return aluno.remover(matricula)
    except Exception as e:
        return str(e)
    return

if __name__ == '__main__':
    app.run(debug=True)