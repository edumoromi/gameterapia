import pygame
import sys, pygame, os

class Image:
    def load_image(image_name):
        """Carrega uma imagem na memoria"""
        fullname = os.path.join("images", image_name)
        print(fullname)
        try:
            image = pygame.image.load(fullname)
        except pygame.error:
            print("Não foi possivel carregar a imagem: ", fullname)
            raise SystemExit
        return image, image.get_rect()
