import pygame
from ClsImage import Image

ingredientes=[(1, "calabresa"), (2, "cebola_roxa"), (3, "chocolate"), (4, "cogumelo"), (5, "molho_tomate"), (6, "ovo"), (7, "peixe"), (8, "tomate"), (9, "queijo")]


def get():
    tamanhoX = Ingrediente.get_rectx()
    return tamanhoX

class Ingrediente(pygame.sprite.Sprite):
    def __init__(self, startpos,image):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Image.load_image(ingredientes[image][1] + ".png")
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        self.init_pos = startpos

    def update(self):
        self.rect.y = self.rect.y + 2

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def move(self,speed): #AJUSTAR FUNCAO
        self.control(0,speed)