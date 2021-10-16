import pygame

import random

from ClsImage import Image
from ClsGame import Game

def get():
    tamanhoX = Ingrediente.get_rectx()
    return tamanhoX

class Ingrediente(pygame.sprite.Sprite):
    ingredientes=[(0, "massa"), (1, "calabresa"), (2, "cebola_roxa"), (3, "chocolate"), (4, "cogumelo"), (5, "molho_tomate"), (6, "ovo"), (7, "peixe"), (8, "tomate"), (9, "queijo"), (10,"azeitona_verde"),(11,"azeitona_roxa")]
    def __init__(self, startpos,image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Image.load_image(self.ingredientes[image][1] + ".png")
        #self.image = pygame.transform.scale(self.image,(50,50)) #Muda o tamanho da imagem !!! ERRO DE COLISAO
        self.ingrediente = self.ingredientes[image]
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        self.init_pos = startpos
        self.movex = 0
        self.movey = 0

    def control(self, x, y):
        self.movex += x
        self.movey += y
        
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey


    def pega_ingrediente(self,pizza): #AJUSTAR FUNCAO
        self.control(float(Game.calculo_velocidade_direcao_pizza(pizza,self)),-20)
    
    def solta_ingrediente(self, acertou, pizza):
        if acertou:
            self.image, self.rect = Image.load_image(self.ingrediente[1]+ "_aberta.png")
            self.rect.x = pizza.rect.x + 30
            self.rect.y = pizza.rect.y + 10
            self.movex = 0
            self.movey = 0
        else:
            self.movex = 0
            self.movey = 0
            self.rect.x = self.init_pos[0]
            self.rect.y = self.init_pos[1]

    def solta_ingrediente_esteira(self, acertou, pizza):
        if acertou:
            self.image, self.rect = Image.load_image(self.ingrediente[1]+ "_aberta.png")
            self.rect.x = pizza.rect.x + 30
            self.rect.y = pizza.rect.y + 10
            self.movex = 0
            self.movey = 0
        else:
            self.rect.x = 9000
            self.rect.y = 9000


