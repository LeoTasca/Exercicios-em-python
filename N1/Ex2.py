print('--------------Dados dos Funcionários--------------')
class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0

    def aumenta_salario(self):
        self.salario = self.salario + self.aumento
        print(f'Nome: {self.nome} | Idade: {self.idade} | Novo salário: R${self.salario}')

class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20

class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30

class Testes:
    def testar(self):
        programador = Programador('Leonardo', 27, 4000)
        programador.aumenta_salario()
        analista = Analista('Lara', 22, 2500)
        analista.aumenta_salario()

resultado = Testes()
resultado.testar()