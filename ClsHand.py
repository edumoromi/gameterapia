import pygame
from ClsImage import Image
from ClsGame import Game
from ClsFase import Fase

class Hand(pygame.sprite.Sprite):

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        #direcao: 1=direita, -1=esquerda
        #self.direction = 1
        # #carrega a imagem e a posiciona na tela
        self.image, self.rect = Image.load_image("MaoAberta.png")
        self.image = pygame.transform.scale(self.image,(100,100)) #Muda o tamanho da imagem
        self.rect.centerx = Game.DISPLAY_W
        self.rect.centery = Game.DISPLAY_H - 100
        self.movex = 0
        self.movey = 0
        self.ingrediente = 0
        self.pizzaCenter = []

    #Controla a movimentação da mão
    def control(self, x, y):
        self.movex += x
        self.movey += y

    #Verifica colisão com a tela
    def update(self):
        if (self.rect.x <= Game.DISPLAY_W) & (self.rect.x > -2):
            self.rect.x = self.rect.x + self.movex
            self.rect.y = self.rect.y + self.movey
            #print(self.rect.x,self.rect.y)
        else:
            self.movex =0
            self.movey =0

        # moving left
        #if self.movex < 0:
        #    self.frame += 1
        #    if self.frame > 3*ani:
        #        self.frame = 0
        #    self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

        # moving right
        #if self.movex > 0:
        #    self.frame += 1
        #    if self.frame > 3*ani:
        #        self.frame = 0
        #    self.image = self.images[self.frame//ani]

    def move(self,dir,key,screen): #AJUSTAR FUNCAO
        if key == "DOWN":
            if dir == "RIGHT":
                if self.rect.x <= -2:
                    self.rect.x = 2
                self.control(2,0)
            else:
                if self.rect.x >= Game.DISPLAY_W:
                    self.rect.x = Game.DISPLAY_W
                self.control(-2,0)
        elif key == "UP":
            if dir == "RIGHT":
               self.control(-2,0)
            else:
               self.control(2,0)

    def pega_ingrediente(self,ingrediente,pizzaCenter): #AJUSTAR FUNCAO
        x = self.rect.x
        y = self.rect.y
        self.image, self.rect = Image.load_image("MaoFechada.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x = x
        self.rect.y = y

        #Teste mão andando até a pizza

        fase=Fase()

        if ingrediente == fase.ingredientes[2]:
           self.control(0, -2)

        elif ingrediente == fase.ingredientes[0]:
            self.control(2, -2)
            print(x)

        elif ingrediente == fase.ingredientes[1]:
            self.control(-0.8, -3)
            print(x)

    def solta_ingrediente(self, x, y):
        self.image, self.rect = Image.load_image("MaoAberta.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect.x = x - 60
        self.rect.y = 425
        self.movex = 0
        self.movey = 0

