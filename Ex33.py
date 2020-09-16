import random
import string

notas = {'Leo': [] , 'Maria': [], 'Eduarda': []}
print('--Alunos--')
for key, value in notas.items():
    print(key)

for key, value in notas.items():
    for i in range(3):
        nota = int(input(f'Digite a {i + 1}ª nota do {key}: '))
        value.append(nota)

rm = str(input('Digite o nome do aluno que deseja remover as notas: ')).lower()
removido = False
for key, value in notas.items():
    if key == rm:
        notas[key] = [0]
        removido = True

if removido == True:
    print(f'Nota removida!')
else:
    print('Aluno não encontrado')

alunoAt = str(input('Digite o nome do aluno que deseja atualizar as notas: ')).lower()
permitidoAt = False
for key, value in notas.items():
    if alunoAt == key and value != None:
        permitidoAt = True

if permitidoAt == True:
    listaAt = []
    for i in range(3):
        notaAt = int(input(f'Digite a {i + 1}º nota: '))
        listaAt.append(notaAt)

    atualizado = False
    for key, value in notas.items():
        if key == alunoAt:
            notas[key] = listaAt
            atualizado = True

    if atualizado == True:
        print('Nota atualizada!')
else:
    print('Ação não executada! Verifique novamente!')


alunoAd = str(input('Digite o nome do aluno que deseja adicionar as notas: ')).lower()
permitidoAd = False
for key, value in notas.items():
    if alunoAd == key and value == None:
        permitidoAd = True

if permitidoAd == True:
    listaAd = []
    for i in range(3):
        notaAd = int(input(f'Digite a {i + 1}º nota: '))
        listaAd.append(notaAd)

    for key, value in notas.items():
        if key == alunoAd:
            notas[key] = listaAd

        print('Nota adicionada!')
else:
    print('Ação não executada! Verifique novamente!')

print(notas)

for key, value in notas.items():
    print(f'O aluno {key} ficou media igual a {sum(value)/3}')