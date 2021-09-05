from typing import Any

import pygame
from ClsMenu import *
import sys
import time

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD) #Define pinagem física (outra opção BCM)

#GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(40, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

class Game():
    #Tamanho da tela do jogo.
    DISPLAY_W, DISPLAY_H = 800, 600
    clock = pygame.time.Clock()
    black = 255, 255, 255
    size = width, height = DISPLAY_W, DISPLAY_H
    screen = pygame.display.set_mode(size)
    lista_ingredientes = []
    Pizza = ""
    Hand = ""
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
        self.delay =0
        self.trava = 0
        self.entrou = False
        self.segurando = False


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

    def colisao_ingrediente(self,objeto):
        for i in (self.lista_ingredientes):
            if self.Hand.rect.colliderect(i.rect):
                objeto[0] = i
                return True
        return False

    def checa_eventos_teclado(self):
        Objeto = [None]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.Hand.move("LEFT", "DOWN", self.size)
                if event.key == pygame.K_RIGHT:
                    self.Hand.move("RIGHT", "DOWN", self.size)
                if event.key == pygame.K_SPACE:
                    if self.colisao_ingrediente(Objeto):
                        self.Hand.pega_ingrediente(Objeto)
                        self.Hand.pegou = True
                        self.Hand.ingrediente = Objeto[0]
                        print(Objeto[0].name)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.Hand.move("LEFT", "UP", self.size)
                if event.key == pygame.K_RIGHT:
                    self.Hand.move("RIGHT", "UP", self.size)
                if event.key == pygame.K_SPACE:
                    if self.Hand.pegou:
                        self.Hand.pegou = False
                        if self.Pizza.rect.colliderect(self.Hand.rect):
                            self.Pizza.solta_ingrediente(self.Hand.ingrediente)
                            self.Hand.solta_ingrediente()
                        else:
                            self.Hand.solta_ingrediente()

    def checa_eventos_push(self):
        Objeto = [None]
        self.delay += 1
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)  # Define pinagem física (outra opção BCM)

        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print(self.trava)
        print(self.delay)
        if (GPIO.input(40) == 1) & (self.delay > self.trava):
            self.Hand.move("LEFT", "DOWN", self.size)
            self.trava = self.delay
            self.entrou = True

        if (GPIO.input(8) == 1) & (self.delay > self.trava):
            self.Hand.move("RIGHT", "DOWN", self.size)
            self.trava = self.delay
            self.entrou = True

        if (GPIO.input(10) == 1) & (self.delay > self.trava):
            self.segurando = True
            if self.colisao_ingrediente(Objeto):
                self.Hand.pega_ingrediente(Objeto)
                self.Hand.pegou = True
                self.Hand.ingrediente = Objeto[0]

        if self.Hand.pegou & (self.segurando == False):
            self.Hand.pegou = False
            if self.Pizza.rect.colliderect(self.Hand.rect):
                self.Pizza.solta_ingrediente(self.Hand.ingrediente)
                self.Hand.solta_ingrediente()

            else:
                self.Hand.solta_ingrediente()

        if (self.delay > self.trava) & (self.entrou == True) & (self.segurando == False):
            self.Hand.para_mao()
            self.entrou = False
        self.segurando = False


    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def update_ingredientes(self):
        for i in (self.lista_ingredientes):
            # i.move(2)
            i.update()
            self.screen.blit(i.image, i.rect)
    def cria_igredientes(self):
        from ClsIngrediente import Ingrediente
        self.lista_ingredientes.append(Ingrediente([self.DISPLAY_H/1.5,self.DISPLAY_W/1.7],"MolhoTomate.png"))
        self.lista_ingredientes.append(Ingrediente([self.DISPLAY_H/2.0,self.DISPLAY_W/1.7],"calabresa.png"))
        self.lista_ingredientes.append(Ingrediente([self.DISPLAY_H/1.2,self.DISPLAY_W/1.7],"cogumelo.png"))
        self.lista_ingredientes.append(Ingrediente([self.DISPLAY_H / 3, self.DISPLAY_W / 1.7],"tomate.png"))
        self.lista_ingredientes.append(Ingrediente([self.DISPLAY_H/6,self.DISPLAY_W/1.7],"massa.png"))

    def in_game_loop(self):
        from ClsHand import Hand
        from ClsPizza import Pizza
        from ClsIngrediente import Ingrediente
        from ClsFase import Fase

        pegou = False #AJUSTAR VARIAVEL

        #Instanciando a Pizza e a mão
        #Pizza = Pizza([(self.DISPLAY_W / 1.9), (self.DISPLAY_W * 1/6)])
        #Hand = Hand([self.DISPLAY_H/10,self.DISPLAY_W/1.5])
        Hand.pizzaCenter = Pizza.rect.center

        #Instanciando os ingredientes
        Molho = Ingrediente([self.DISPLAY_H/1.5,self.DISPLAY_W/1.7],"MolhoTomate.png")
        calabresa = Ingrediente([self.DISPLAY_H/2.0,self.DISPLAY_W/1.7],"calabresa.png")
        cogumelo = Ingrediente([self.DISPLAY_H/1.2,self.DISPLAY_W/1.7],"cogumelo.png")
        tomate = Ingrediente([self.DISPLAY_H / 3, self.DISPLAY_W / 1.7],"tomate.png")
        massa = Ingrediente([self.DISPLAY_H/6,self.DISPLAY_W/1.7],"massa.png")


        pegou = False #AJUSTAR VARIAVEL
        delay =0
        self.Pizza = Pizza([(self.DISPLAY_W / 1.9), (self.DISPLAY_W * 1/6)])
        self.Hand = Hand([self.DISPLAY_H/10,self.DISPLAY_W/1.5])
        self.cria_igredientes()

        pygame.display.set_caption('Hand!')

        pygame.mixer.music.load("./images/background.mp3")
        pygame.mixer.music.play()

        while 1:
            # garante que o programa nao vai rodar a mais que 120fps

            self.clock.tick(30)

            self.checa_eventos_teclado()
            #self.checa_eventos_push()

            # atualiza os objetos
            self.Hand.update()

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
