class Classe:
    def igualdade(self, lista1, lista2):
        if lista1 == lista2:
            print('True')
        else:
            print('False')

    def ocorrencia(self, lista1, lista2):
        Ocorrencia_total1 = 0
        for  item in lista1:
            if lista1[0] == item:
                Ocorrencia_total1 += 1
        print(f"Ocorrencias na primeira lista = {Ocorrencia_total1}") 

        Ocorrencia_total2 = 0
        for item in lista2:
            if lista2[0] == item:
                Ocorrencia_total2 += 1
        print(f"Ocorrencias na segunda lista = {Ocorrencia_total2}") 
    
resultado = Classe()

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 6, 6, 6, 6]
resultado.igualdade(lista1, lista2)
resultado.ocorrencia(lista1, lista2)