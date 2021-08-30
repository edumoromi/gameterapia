import pygame
from ClsMenu import *
import sys

import time
class Game():
    #Tamanho da tela do jogo.
    DISPLAY_W, DISPLAY_H = 800, 600

    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.size = self.DISPLAY_W, self.DISPLAY_H
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        #self.font_name = '8-BIT WONDER.TTF'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        # Teste som

        self.sound = pygame.mixer.Sound('./images/error.mp3')

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            pygame.display.update()
            self.reset_keys()
            self.in_game_loop()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def in_game_loop(self):
        from ClsHand import Hand
        from ClsPizza import Pizza
        from ClsIngrediente import Ingrediente
        from ClsFase import Fase

        pegou = False #AJUSTAR VARIAVEL

        #Instanciando a Pizza e a mão
        Pizza = Pizza([(self.DISPLAY_W / 1.9), (self.DISPLAY_W * 1/6)])
        Hand = Hand([self.DISPLAY_H/10,self.DISPLAY_W/1.5])
        Hand.pizzaCenter = Pizza.rect.center

        #Instanciando os ingredientes
        Molho = Ingrediente([self.DISPLAY_H/1.5,self.DISPLAY_W/1.7],"MolhoTomate.png")
        calabresa = Ingrediente([self.DISPLAY_H/2.0,self.DISPLAY_W/1.7],"calabresa.png")
        cogumelo = Ingrediente([self.DISPLAY_H/1.2,self.DISPLAY_W/1.7],"cogumelo.png")
        tomate = Ingrediente([self.DISPLAY_H / 3, self.DISPLAY_W / 1.7],"tomate.png")
        massa = Ingrediente([self.DISPLAY_H/6,self.DISPLAY_W/1.7],"massa.png")

        pygame.display.set_caption('Hand!')
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.size)
        black = 255, 255, 255

        pygame.mixer.music.load("./images/background.mp3")
        pygame.mixer.music.play()

        while 1:
            # garante que o programa nao vai rodar a mais que 120fps
            clock.tick(120)

            # checa eventos de teclado
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                if Hand.rect.colliderect(Pizza.rect):
                    Pizza.solta_ingrediente(ingrediente)
                    Hand.solta_ingrediente(pos[0], pos[1])
                    pegou = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Hand.move("LEFT","DOWN",self.size)

                    elif event.key == pygame.K_RIGHT:
                        Hand.move("RIGHT","DOWN",self.size)

                    elif event.key == pygame.K_SPACE:

                        Hand.ingrediente = 1;
                        pos = Hand.rect.center
                        if Hand.rect.colliderect(Molho.rect):
                            Hand.pega_ingrediente("molho", Hand.pizzaCenter)
                            pegou = True
                            ingrediente = "molho"
                        elif Hand.rect.colliderect(massa.rect):
                            Hand.pega_ingrediente("massa", Hand.pizzaCenter)
                            pegou = True
                            ingrediente = "massa"
                        elif Hand.rect.colliderect(cogumelo.rect):
                            Hand.pega_ingrediente("cogumelo", Hand.pizzaCenter)
                            pegou = True
                            ingrediente = "cogumelo"

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        Hand.move("LEFT","UP",self.size)

                    if event.key == pygame.K_RIGHT:
                        Hand.move("RIGHT","UP",self.size)

                    if event.key == pygame.K_SPACE:
                        if pegou:
                            self.sound.play()
                            pegou = False
                            Hand.solta_ingrediente(pos[0], pos[1])

            # atualiza os objetos
            Hand.update()

            # redesenha a tela
            screen.fill(black)
            screen.blit(Pizza.image, Pizza.rect)
            screen.blit(Molho.image, Molho.rect)
            screen.blit(calabresa.image,calabresa.rect)
            screen.blit(cogumelo.image,cogumelo.rect)
            screen.blit(tomate.image,tomate.rect)
            screen.blit(massa.image,massa.rect)
            screen.blit(Hand.image, Hand.rect)


            pygame.display.flip()