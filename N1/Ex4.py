'''Um decorator é uma forma prática e reusável de adicionarmos funcionalidades às nossas funções/métodos/classes, sem precisarmo alterar o código delas.
O decorator é uma ferramente muito poderosa e útil em Python, pois permite que os programadores modifiquem o comportamento da função ou classe. 
Os decorators nos permitem encapsular outra função para estender o comportamento da função encapsulada, sem modificá-la permanentemente.
Em decorators, as funções são tomadas como argumento para outra função e então chamadas dentro da função de encapsulamento.'''

'''Padrão de projeto é uma solução geral para um problema que ocorre com frequência dentro de um determinado contexto no projeto de software.
O arquiteto Christopher Alexander coloca que um padrão de projeto deve ter, idealmente, as seguintes características: 
Encapsulamento, Generalidade, Equilíbrio, Abstração, Abertura e Combinatoriedade, 
sendo assim robusto para resolver um problema pequeno ou grande e específico para resolver um problema singular.
A Linguagem Python é ótima para aplicar padrões de projeto, principalmente por ser orienta a objetos, ter tipagem dinâmica, dentre outras coisas.'''

import datetime
import random

def calculate_time_decorator(function):
    def calculate_time():
        print(datetime.datetime.now())
        function()
        print(datetime.datetime.now())

    return calculate_time

@calculate_time_decorator
def my_function():
    numbers = []
    for i in range(4):
        number = random.randint(0,10)
        numbers.append(number)
        print(f'O {i+1}º número gerado foi {number}')
    print('A soma dos números é', sum(numbers))
my_function()