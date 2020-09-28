class TraduzirMensagem:
    def Tradutor(self, lista):
        codigo = []
        for item in lista:
            if item == 0:
                codigo.append(' ')
            elif item == 1:
                codigo.append('a')
            elif item == 2:
                codigo.append('b')
            elif item == 3:
                codigo.append('c')
            elif item == 4:
                codigo.append('d')
            elif item == 5:
                codigo.append('e')
            elif item == 6:
                codigo.append('f')
            elif item == 7:
                codigo.append('g')
            elif item == 8:
                codigo.append('h')
            elif item == 9:
                codigo.append('i')
            elif item == 10:
                codigo.append('j')
            elif item == 11:
                codigo.append('k')
            elif item == 12:
                codigo.append('l')
            elif item == 13:
                codigo.append('m')
            elif item == 14:
                codigo.append('n')
            elif item == 15:
                codigo.append('o')
            elif item == 16:
                codigo.append('p')
            elif item == 17:
                codigo.append('q')
            elif item == 18:
                codigo.append('r')
            elif item == 19:
                codigo.append('s')
            elif item == 20:
                codigo.append('t')
            elif item == 21:
                codigo.append('u')
            elif item == 22:
                codigo.append('v')
            elif item == 23:
                codigo.append('w')
            elif item == 24:
                codigo.append('x')
            elif item == 25:
                codigo.append('y')
            elif item == 26:
                codigo.append('z')
        print(f'Mensagem: {codigo}')

resultado = TraduzirMensagem()
mensagem_secreta = [12, 5, 15, 0, 20, 1, 19, 3, 1]
resultado.Tradutor(mensagem_secreta)