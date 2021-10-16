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

        #self.molho = pygame.image.load_image('molho.png')
        #self.molho.convert()

    def solta_ingrediente(self,ingrediente):
        x = self.rect.x
        y = self.rect.y
        ingrediente.control(0,0)

    def retorna_altura_imagem_pizza(self):
        tamanho=self.image.get_size()
        return tamanho[1]
