import pygame

import random

from ClsImage import Image


def get():
    tamanhoX = Ingrediente.get_rectx()
    return tamanhoX

class Ingrediente(pygame.sprite.Sprite):
    ingredientes=[(0, "massa"), (1, "calabresa"), (2, "cebola_roxa"), (3, "chocolate"), (4, "cogumelo"), (5, "molho_tomate"), (6, "ovo"), (7, "peixe"), (8, "tomate"), (9, "queijo")]
    def __init__(self, startpos,image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Image.load_image(self.ingredientes[image][1] + ".png")
        #self.image = pygame.transform.scale(self.image,(50,50)) #Muda o tamanho da imagem !!! ERRO DE COLISAO
        self.ingrediente = image
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

    def calculo_velocidade(self,Vy, Px,Py):
       Vx = (Px-self.rect.x) * Vy / (Py-self.rect.y)
       return Vx

    def pega_ingrediente(self): #AJUSTAR FUNCAO
       self.control(float(self.calculo_velocidade(-20, 380,67)),float(-20))
    
    def solta_ingrediente(self):
        self.movex = 0
        self.movey = 0

