#Chute um número até acertar !

import random
import PySimpleGUI as PSG

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
    
    def Iniciar(self):
        #Layout
        layout = [
            [PSG.Text('Seu chute: ', size=(20,0))],
            [PSG.Input(size=(18,0), key='ValorChute')],
            [PSG.Button('Chutar')],
            [PSG.Output(size=(30,10))]
        ]
        #Janela
        self.janela = PSG.Window('Chute o numero! ', layout)
        self.GerarNumeroAleatorio()

        try:
            while True:   
                #Receber os valores
                self.eventos, self.valores = self.janela.Read()
                if self.eventos == 'Chutar':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor menor! ')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor maior! ')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            print('Parabéns, você acertou! ')
                            self.tentar_novamente = False
                            break
                        # Window close button event
                elif self.eventos == PSG.WIN_CLOSED:    
                    break
        except:
            print('Chute um valor válido (1 a 100)')
            self.Iniciar()
   
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()