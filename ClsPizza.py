import pygame
from ClsImage import Image


def get():
    tamanhoX = Pizza.get_rectx()
    return tamanhoX

class Pizza(pygame.sprite.Sprite):
    """classe para a bola"""

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Image.load_image('bandeja.png')
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        self.init_pos = startpos

    def solta_ingrediente(self,ingrediente):
        x = self.rect.x
        y = self.rect.y
        if ingrediente.name == "massa.png":
            self.image, self.rect = Image.load_image('pizza_massa.png')
        elif ingrediente.name == "MolhoTomate.png":
            self.image, self.rect = Image.load_image('pizza_molho.png')
        elif ingrediente.name == "cogumelo.png":
            self.image, self.rect = Image.load_image('pizza_cogumelo.png')
        self.rect.x = x
        self.rect.y = y