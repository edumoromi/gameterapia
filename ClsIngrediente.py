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
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        self.init_pos = startpos
        self.movex = 0
        self.movey = 0

    def control(self, x, y):
        self.movex += x
        self.movey += y
        
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
