import math

class Classe:
    def media(self, lista):
        total = 0
        for item in lista:
            total += item
        media = total / len(lista)

        print('media',media)
        for item in lista:
            if math.isclose(item, media, abs_tol = 5.5):
                print(f'O valor mais próximo da media é {media} = {item}')

    
resultado = Classe()

lista = [2.5, 7.5, 10, 4]
resultado.media(lista)