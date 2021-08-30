import pygame
import random
from ClsImage import Image

def get():
    tamanhoX = Ingrediente.get_rectx()
    return tamanhoX

class Ingrediente(pygame.sprite.Sprite):

    def __init__(self, startpos,image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Image.load_image(image)
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        self.init_pos = startpos


