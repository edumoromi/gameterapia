import sys, pygame, os
pygame.init()

from ClsGame import Game
g = Game()

while g.running:
    pygame.display.set_caption('Italian Chef')
    g.curr_menu.display_menu()
    g.game_loop("Mesa",3)


# cria os nossos objetos (bola e Hand)



