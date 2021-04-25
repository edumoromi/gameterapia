import pygame
from ClsImage import Image
size = width, height = 6000, 4000
class Pizza(pygame.sprite.Sprite):
    """classe para a bola"""

    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.speed = [2, 2]
        self.image, self.rect = Image.load_image('pizza.jpg')
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        self.init_pos = startpos

    def update(self,size):
        self.rect.move_ip(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
        if self.rect.bottom > size[1]:
            self.rect.centerx = self.init_pos[0]
            self.rect.centery = self.init_pos[1]
