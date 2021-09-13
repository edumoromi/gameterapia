from typing import Any

import pygame
from ClsMenu import *
import sys
import time
import random
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
    Hand = []
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
        self.contador = 0
        self.entrou = False
        self.segurando = False


        # Teste som

        #self.sound = pygame.mixer.Sound('./images/error.mp3')

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
            if self.Hand[0].rect.colliderect(i.rect):
                objeto[0] = i
                return True
        return False

    def colisao_ingrediente(self,objeto,Hand):
        for i in (self.lista_ingredientes):
            if Hand.rect.colliderect(i.rect):
                objeto[0] = i
                return True
        return False

    def checa_eventos_teclado(self,Fase):
        if (Fase.jogo != "esteira") & (Fase.movimentacao_automatica == True)  & (Fase.segurar_ao_clicar == True):
            Objeto = [None]

            if self.Hand[0].rect.x <= 700:
                self.Hand[0].move("RIGHT", "DOWN", self.size)
                self.Hand[0].move("LEFT", "DOWN", self.size)
            print(self.Hand[0].rect.x)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.colisao_ingrediente(Objeto,self.Hand[0]):
                            #self.Hand.inix = self.Hand.movex #!!!
                            #self.Hand.iniy = self.Hand.movey #!!!
                            self.Hand[0].pega_ingrediente(Objeto[0])
                            Objeto[0].pega_ingrediente()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if self.Hand[0].pegou:
                            self.Hand[0].pegou = False
                            if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                                self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                                self.Hand[0].solta_ingrediente()
                                #self.Hand[0].ingrediente.solta_ingrediente()
                                #self.Hand.i = 0  # !!!
                            else:
                                self.Hand[0].solta_ingrediente()
                                self.Hand[0].i = 0  # !!!

        if (Fase.jogo == "esteira") & (Fase.movimentacao_automatica == True) & (Fase.segurar_ao_clicar == True):
            Objeto = [None]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT) & (self.colisao_ingrediente(Objeto,self.Hand[0])):
                        #self.Hand.inix = self.Hand.movex #!!!
                        #self.Hand.iniy = self.Hand.movey #!!!
                        self.Hand[0].pega_ingrediente(Objeto[0])
                        Objeto[0].pega_ingrediente()
                    if (event.key == pygame.K_RIGHT) & (self.colisao_ingrediente(Objeto,self.Hand[1])):
                        self.Hand[1].pega_ingrediente(Objeto[0])
                        Objeto[0].pega_ingrediente()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if self.Hand[0].pegou:
                            self.Hand[0].pegou = False
                            if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                                self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                                self.Hand[0].solta_ingrediente()
                                #self.Hand[0].ingrediente.solta_ingrediente()
                                #self.Hand.i = 0  # !!!
                            else:
                                self.Hand[0].solta_ingrediente()
                                self.Hand[0].i = 0  # !!!
                    if event.key == pygame.K_RIGHT:
                        if self.Hand[1].pegou:
                            self.Hand[1].pegou = False
                            if self.Pizza.rect.colliderect(self.Hand[1].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                                self.Pizza.solta_ingrediente(self.Hand[1].ingrediente)
                                self.Hand[1].solta_ingrediente()
                                #self.Hand[0].ingrediente.solta_ingrediente()
                                #self.Hand.i = 0  # !!!
                            else:
                                self.Hand[1].solta_ingrediente()
                                self.Hand[1].i = 0  # !!!


        if (Fase.jogo != "esteira") & (Fase.movimentacao_automatica == False)  & (Fase.segurar_ao_clicar == True):
            Objeto = [None]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.Hand[0].move("LEFT", "DOWN", self.size)
                    if event.key == pygame.K_RIGHT:
                        self.Hand[0].move("RIGHT", "DOWN", self.size)
                    if event.key == pygame.K_SPACE:
                        if self.colisao_ingrediente(Objeto,self.Hand[0]):
                            #self.Hand.inix = self.Hand.movex #!!!
                            #self.Hand.iniy = self.Hand.movey #!!!
                            self.Hand[0].pega_ingrediente(Objeto[0])
                            Objeto[0].pega_ingrediente()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.Hand[0].move("LEFT", "UP", self.size)
                    if event.key == pygame.K_RIGHT:
                        self.Hand[0].move("RIGHT", "UP", self.size)
                    if event.key == pygame.K_SPACE:
                        if self.Hand[0].pegou:
                            self.Hand[0].pegou = False
                            if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                                self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                                self.Hand[0].solta_ingrediente()
                                #self.Hand[0].ingrediente.solta_ingrediente()
                                #self.Hand.i = 0  # !!!
                            else:
                                self.Hand[0].solta_ingrediente()
                                self.Hand[0].i = 0  # !!!
    

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
    def cria_igredientes(self,Fase):
        from ClsIngrediente import Ingrediente
        print(Fase.jogo)
        if Fase.jogo == "esteira":
            if self.contador % 100 == 0:
                ingrediente = Ingrediente([150,50], random.randint(1,8))
                self.lista_ingredientes.append(ingrediente)
                ingrediente.control(0,2)
                ingrediente = Ingrediente([self.DISPLAY_W/1.2,50], random.randint(1,8))
                ingrediente.control(0,2)
                self.lista_ingredientes.append(ingrediente)
        else:
            qtdingredientes = len(Fase.lista_ingredientes) +1
            if self.contador % 1000 == 0:
                for ingrediente_pizza in Fase.lista_ingredientes:
                    self.lista_ingredientes.append(Ingrediente([self.DISPLAY_W/qtdingredientes,self.DISPLAY_H/1.3],ingrediente_pizza[0]))
                    qtdingredientes -=1

        self.contador +=1
              


    def cria_objetos(self,Fase):
        from ClsPizza import Pizza
        self.Pizza = Pizza([(self.DISPLAY_W / 1.9), (self.DISPLAY_W * 1/6)])
        #self.Hand = Hand([self.DISPLAY_H/10,self.DISPLAY_W/1.5])
        #self.Hand.pizzaCenter = self.Pizza.rect.center
        #self.cria_igredientes(Fase)
        self.cria_maos(Fase)

    def cria_maos(self,ObjFase):
       from ClsHand import Hand
       for localizacao in ObjFase.localizacao_mao:
            self.Hand.append(Hand([self.DISPLAY_W/localizacao[0],self.DISPLAY_H/localizacao[1]]))

    def atualiza_objetos(self,Fase):
        self.atualiza_maos(Fase)


    def atualiza_maos(self,Fase):
        for mao in self.Hand:
            mao.update()


    def desenha_tela(self):
        self.screen.fill(self.black)
        self.screen.blit(self.Pizza.image, self.Pizza.rect)
        self.update_ingredientes()
        for mao in self.Hand:
            self.screen.blit(mao.image, mao.rect)


    def in_game_loop(self):
        from ClsFase import Fase
        #ObjFase = Fase(2,"esteira")
        #ObjFase = Fase(4,"")
        ObjFase = Fase(2,"")

        self.cria_objetos(ObjFase)
        contador =0
        #pygame.mixer.music.load("./images/background.mp3")
        #pygame.mixer.music.play()

        while 1: #!!! QUEBRAR QUANDO FASE ACABAR
            self.clock.tick(30)
            self.cria_igredientes(ObjFase)

            self.checa_eventos_teclado(ObjFase)
            #self.checa_eventos_push()

            # atualiza os objetos
            self.atualiza_objetos(ObjFase)
            #self.Hand.update()

            self.desenha_tela()
            pygame.display.flip()