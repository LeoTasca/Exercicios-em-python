while True:
    nota = int(input('Inserir uma nota entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('NOTA INVÁLIDA! Por favor inserir nota entre 0 e 10')
    print('Nota inserida com sucesso!')
    break