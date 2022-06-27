#Chute um número até acertar !

import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
    
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor menor! ')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor maior! ')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) == self.valor_aleatorio:
                    print('Parabéns, você acertou! ')
                    self.tentar_novamente = False
        except:
            print('Chute um valor válido (1 a 100)')
            self.Iniciar()
   
    def PedirValorAleatorio(self):
        self.valor_do_chute = int(input('Chute um número entre 1 e 100: '))
        
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()