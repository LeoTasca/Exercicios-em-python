class Classe:
    def Metade(self, lista):

        print(f"Resultado = {lista[5:] + lista[:5]}")

        
    
resultado = Classe()

lista = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

resultado.Metade(lista)