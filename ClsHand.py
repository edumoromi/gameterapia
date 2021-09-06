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
        self.image = pygame.transform.scale(self.image,(100,100)) #Muda o tamanho da imagem
        self.rect.centerx = Game.DISPLAY_W
        self.rect.centery = Game.DISPLAY_H - 100
        self.movex = 0.000
        self.movey = 0.000
        self.ingrediente = 0
        self.pizzaCenter = []
        self.pegou = False
        self.inix = 0
        self.iniy  = 0
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




    def calculo_velocidade(self,Vy, Px,Py):
        Vx = (Px-self.rect.x) * Vy / (Py-self.rect.y)
        return Vx

    def move(self,dir,key,screen): #AJUSTAR FUNCAO
        if key == "DOWN":
            if dir == "RIGHT":
                if self.rect.x <= -2:
                    self.rect.x = 2
                if self.movex != 2:
                    self.control(2,0)
            else:
                if self.rect.x >= Game.DISPLAY_W:
                    self.rect.x = Game.DISPLAY_W
                if self.movex != -2:
                    self.control(-2,0)

        elif key == "UP":

            self.para_mao()
    def pega_ingrediente(self,ingrediente): #AJUSTAR FUNCAO

        x = self.rect.x
        y = self.rect.y
        self.image, self.rect = Image.load_image("MaoFechada.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x = x
        self.rect.y = y


        #Teste mão andando até a pizza

        #fase=Fase()


        print(ingrediente[0].name)
        self.control(float(self.calculo_velocidade(-20, 380,67)),float(-20))

    def solta_ingrediente(self):
        x = self.rect.x
        y = self.rect.y
        self.image, self.rect = Image.load_image("MaoAberta.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x = 360
        self.rect.y = 430
        self.para_mao()
        self.ingrediente = None
        print(x,y)

    def para_mao(self):
        self.movex = 0
        self.movey = 0



        

