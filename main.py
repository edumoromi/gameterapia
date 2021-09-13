import sys, pygame, os
pygame.init()

from ClsGame import Game
g = Game()

while g.running:
    import os; print(os.getcwd()) # mostra o diretorio atual
    pygame.display.set_caption('Italian Chef')
    g.curr_menu.display_menu()
    g.game_loop()


# cria os nossos objetos (bola e Hand)



