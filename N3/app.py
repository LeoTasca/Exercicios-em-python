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
@app.route(f"/aluno/save", methods=['POST'])
def cadastrarAluno():
    nome = request.args.get('nome')
    matricula = request.args.get('matricula')
    try:
        return aluno.cadastrar(nome, matricula)
    except Exception as e:
        return str(e)
    return

#post para consultar
@app.route("/alunos", methods=['GET'])
def consultarAluno():
    alunos = aluno.consultar()
    return jsonify(alunos)

#post para editar
@app.route(f"/aluno/update", methods=['PUT'])
def editarAluno():
    matricula = request.args.get('matricula')
    try:
        return aluno.editar(matricula)
    except Exception as e:
        return str(e)
    return

#post para remover
@app.route(f"/aluno/delete", methods=['DELETE'])
def removerAluno():
    matricula = request.args.get('matricula')
    try:
        return aluno.remover(matricula)
    except Exception as e:
        return str(e)
    return

if __name__ == '__main__':
    app.run(debug=True)