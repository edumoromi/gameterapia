import pygame
from ClsImage import Image
size = width, height = 6000, 4000 #Não está sendo usado para nada

def get():
    tamanhoX = Pizza.get_rectx()
    return tamanhoX

class Pizza(pygame.sprite.Sprite):
    """classe para a bola"""

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Image.load_image('pizza.jpg')
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        self.init_pos = startpos