import pygame
from ClsImage import Image
from ClsGame import Game
from ClsFase import Fase


class Hand(pygame.sprite.Sprite):

    velocidade_x = 0 #criar funaco get e set
    velocidade_y = 0 #criar funaco get e set
    ingrediente = None
    #cont =0

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        #direcao: 1=direita, -1=esquerda
        #self.direction = 1
        # #carrega a imagem e a posiciona na tela
        self.image, self.rect = Image.load_image("MaoAberta.png")
        #self.image = pygame.transform.scale(self.image,(100,100)) #Muda o tamanho da imagem !!! ERRO DE COLISAO
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        self.movex = 0.000
        self.movey = 0.000
        self.ingrediente = 0
        self.pizzaCenter = []
        self.pegou = False
        self.inix = startpos[0]
        self.iniy  = startpos[1]
        self.i = 0
    #Controla a movimentação da mão
    def control(self, x, y):
        self.movex += x
        self.movey += y

    #def control2(self, x, y): !Calculo Nags
    #    self.i +=1
    #    self.movex = self.inix + x * self.i
    #    self.movey = self.iniy + y * self.i
    #    print(type(self.movex))





    #Verifica colisão com a tela
    def update(self):
        #self.cont = self.cont +1
        if (self.rect.x <= Game.DISPLAY_W) & (self.rect.x > -2):
            self.rect.x = self.rect.x + self.movex
            self.rect.y = self.rect.y + self.movey

        else:
            self.movex =0
            self.movey =0

    def move(self,dir,key,screen): #AJUSTAR FUNCAO
        if key == "DOWN":
            if dir == "RIGHT":
                if self.rect.x <= -2:
                    self.rect.x = 2
                if (self.movex != 2)  & (self.movex != 4):
                    self.control(4,0)
            else:
                if self.rect.x >= Game.DISPLAY_W:
                    self.rect.x = Game.DISPLAY_W
                if (self.movex != -2) & (self.movex != -4):
                    self.control(-4,0)

        elif (key == "UP") & (self.pegou == False):
            self.para_mao()

    def pega_ingrediente(self,ingrediente,pizza): #AJUSTAR FUNCAO
        self.para_mao()
        x = self.rect.x
        self.inix = x
        y = self.rect.y
        self.iniy = y 
        self.image, self.rect = Image.load_image("MaoFechada.png")
       # self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x = x
        self.rect.y = y
        self.control(float(Game.calculo_velocidade_direcao_pizza(pizza,self)),-20)
        self.ingrediente = ingrediente
        self.pegou = True

    def solta_ingrediente(self, acertou = False, Pizza = None):
        self.image, self.rect = Image.load_image("MaoAberta.png")
        #self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x = self.inix
        self.rect.y = self.iniy
        self.para_mao()
        self.ingrediente.solta_ingrediente(acertou, Pizza)
        self.ingrediente = None
        self.pegou = False

    def solta_ingrediente_esteira(self, acertou = False, Pizza = None):
        self.image, self.rect = Image.load_image("MaoAberta.png")
        #self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x = self.inix
        self.rect.y = self.iniy
        self.para_mao()
        self.ingrediente.solta_ingrediente_esteira(acertou, Pizza)
        self.ingrediente = None
        self.pegou = False

    def para_mao(self):
        self.movex = 0
        self.movey = 0

    def retorna_largura_imagem_mao(self):
        tamanho=self.image.get_size()
        return tamanho[0]



        

