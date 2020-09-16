class Classe:
    def maior(self, lista):
        print(f"Maior = {max(lista)}")

    def soma(self, lista):
        Soma_total = 0
        for item in lista:
            Soma_total += item
        print(f"Total = {Soma_total}")
    
    def ocorrencia(self, lista):
        Ocorrencia_total = 0
        for  item in lista:
            if lista[0] == item:
                Ocorrencia_total += 1
        print(f"Ocorrencias = {Ocorrencia_total}")
    
    def media(self, lista):
        total = 0
        for item in lista:
            total += item
        media = total / len(lista)
        print(f"Media = {media}")
        
    
resultado = Classe()

lista = [3,4,5,7,1,3,2,9,55,44,10,99,3,2]
print(f'List = {lista}')
resultado.maior(lista)
resultado.soma(lista)
resultado.ocorrencia(lista)
resultado.media(lista)