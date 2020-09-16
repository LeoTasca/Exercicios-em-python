import math

class Classe:
    def remove(self, dict):
       del dict['Fabio']
       print(f'Resultado = {dict}')

    
resultado = Classe()

dict = {'Leo': 'Engenheiro', 'Joao': 'Policial', 'Maria': 'Advogada', 'Eduarda': 'Vendedora', 'Fabio': 'Medico'}
resultado.remove(dict)