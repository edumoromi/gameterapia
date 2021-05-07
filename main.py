import sys, pygame, os
pygame.init()
from ClsGame_Esteira import Game
g = Game()
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
# cria os nossos objetos (bola e Hand)




if __name__ == "__main__":
    main()