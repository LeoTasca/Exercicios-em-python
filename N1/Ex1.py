listapresos = []
media = 0
for i in range(12):
    listapresos.append(int(input(f'Quantos reféns foram presos no {i + 1}º mês: ')))
    if i == 0:
        max = min = listapresos[i]
    else:
        if listapresos[i] > max:
            max = listapresos[i]
        if listapresos[i] < min:
            min = listapresos[i]
print(f'O menor número de reféns capturados foi {min}')
print(f'O maior número de reféns capturados foi {max}')

for i in range(len(listapresos)):
    media = media + listapresos[i]
media = media/len(listapresos)
print(f'A média de reféns presos é {media}')

lista_valorprox = []
valor_prox = {valor: abs(valor - media) for valor in listapresos}
for i in valor_prox:
    k = (i, valor_prox[i])
    lista_valorprox.append(k)

num_prox = num_index = 0
for key, value in enumerate(lista_valorprox):
    if key == 0:
        num_prox = value
    else:
        if value < num_prox:
            num_prox = value
            num_index = key
print(f'O valor mais próximo da média de reféns presos é {listapresos[num_index]}')