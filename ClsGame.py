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
    DISPLAY_W, DISPLAY_H = 1280, 720
    clock = pygame.time.Clock()
    black = 255, 255, 255
    size = width, height = DISPLAY_W, DISPLAY_H
    screen = pygame.display.set_mode(size)
    lista_ingredientes = []
    Pizza = ""
    Hand = []
    mov = "D" 
    fonte = pygame.font.SysFont('Roboto', 25)
    fonteScore = pygame.font.SysFont('Comic Sans MS', 20)
    texto = ""
    score = ""
    frame = 30
    usuario = ""

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
        self.delay_e = 0
        self.delay_d = 0
        self.trava_ing =0
        self.trava = 0
        self.trava_e = 0
        self.trava_d = 0
        self.contador = 0
        self.entrou = False
        self.segurando = False
        self.receita =""
        self.erroIngrediente = 0
        self.erroMovimento = 0
        # Teste som

        #self.sound = pygame.mixer.Sound('./images/error.mp3')

    def game_loop(self,jogo,fase):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            pygame.display.update()
            self.reset_keys()
            self.in_game_loop(jogo,fase)

    def check_events(self, menu = None):
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
            if menu != None:
                if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                    if menu.input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                        menu.active = not menu.active
                    else:
                        menu.active = False
                # Change the current color of the input box.
                menu.color = menu.color_active if menu.active else menu.color_inactive
                if event.type == pygame.KEYDOWN:
                    if menu.active:
                        if event.key == pygame.K_RETURN:
                            print("APAGA")
                            menu.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            menu.text = menu.text[:-1]
                        else:
                            menu.text += event.unicode

    def colisao_ingrediente(self,objeto,Hand):
        for i in (self.lista_ingredientes):
            if Hand.rect.colliderect(i.rect):
                objeto[0] = i
                return True
        return False

    def colisao_mao(self,objeto,Hand):
        if Hand.rect.colliderect(objeto.rect):
            return True
        return False


    def checa_eventos_teclado(self,Fase):
        if (Fase.jogo != "esteira") & (Fase.movimentacao_automatica == True)  & (Fase.segurar_ao_clicar == False): #FASE 1
            Objeto = [None]
            if self.Hand[0].pegou == False:
                if (self.Hand[0].rect.x <= self.DISPLAY_W - self.Hand[0].retorna_largura_imagem_mao()) & (self.mov == "D"):
                    self.Hand[0].move("RIGHT", "DOWN", self.size)
                elif (self.Hand[0].rect.x >= self.DISPLAY_W - self.Hand[0].retorna_largura_imagem_mao())  & (self.mov == "D"):
                    self.mov = "E"
                    self.Hand[0].movex = 0
                elif (self.Hand[0].rect.x >= 0) & (self.mov == "E"):
                    self.Hand[0].move("LEFT", "DOWN", self.size)
                    self.mov = "E"
                elif self.Hand[0].rect.x <= 0 & (self.mov == "E"):
                    self.mov = "D"
                    self.Hand[0].movex = 0
            if self.Hand[0].pegou:
                if self.trava >= 18:
                    if self.Pizza.rect.colliderect(self.Hand[0].rect):
                        if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                            Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                            self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                            self.Hand[0].solta_ingrediente(True, self.Pizza)
                            self.trava = 0
                        else:
                            self.erroIngrediente +=1
                            self.Hand[0].solta_ingrediente()
                else:                   
                    self.trava +=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.colisao_ingrediente(Objeto,self.Hand[0]):
                            #self.Hand.inix = self.Hand.movex #!!!
                            #self.Hand.iniy = self.Hand.movey #!!!
                            self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                            Objeto[0].pega_ingrediente(self.Pizza)
                        if self.colisao_mao(self.receita,self.Hand[0]):
                            self.receita.abre_Receita()




        if (Fase.jogo != "esteira") & (Fase.movimentacao_automatica == True)  & (Fase.segurar_ao_clicar == True): #FASE 2
            Objeto = [None]
            if self.Hand[0].pegou == False:
                if (self.Hand[0].rect.x <= self.DISPLAY_W - self.Hand[0].retorna_largura_imagem_mao()) & (self.mov == "D"):
                    self.Hand[0].move("RIGHT", "DOWN", self.size)
                elif (self.Hand[0].rect.x >= self.DISPLAY_W - self.Hand[0].retorna_largura_imagem_mao())  & (self.mov == "D"):
                    self.mov = "E"
                    self.Hand[0].movex = 0
                elif (self.Hand[0].rect.x >= 0) & (self.mov == "E"):
                    self.Hand[0].move("LEFT", "DOWN", self.size)
                    self.mov = "E"
                elif self.Hand[0].rect.x <= 0 & (self.mov == "E"):
                    self.mov = "D"
                    self.Hand[0].movex = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.colisao_ingrediente(Objeto,self.Hand[0]):
                            self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                            Objeto[0].pega_ingrediente(self.Pizza)
                        if self.colisao_mao(self.receita,self.Hand[0]):
                            self.receita.abre_Receita()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if self.Hand[0].pegou:
                            self.Hand[0].pegou = False
                            if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                                if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                                    Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                                    self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                                    self.Hand[0].solta_ingrediente(True, self.Pizza)
                                    self.trava = 0
                                else:
                                    self.erroIngrediente +=1
                                    self.Hand[0].solta_ingrediente()
                            else:
                                self.Hand[0].solta_ingrediente()
                                self.Hand[0].i = 0 
                                self.erroIngrediente +=1

        if (Fase.jogo != "esteira") & (Fase.movimentacao_automatica == False)  & (Fase.segurar_ao_clicar == True): #FASE 3
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
                            self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                            Objeto[0].pega_ingrediente(self.Pizza)
                        if self.colisao_mao(self.receita,self.Hand[0]):
                            self.receita.abre_Receita()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.Hand[0].move("LEFT", "UP", self.size)
                    if event.key == pygame.K_RIGHT:
                        self.Hand[0].move("RIGHT", "UP", self.size)
                    if event.key == pygame.K_SPACE:
                        if self.Hand[0].pegou:
                            self.Hand[0].pegou = False
                            if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                                if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                                    Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                                    self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                                    self.Hand[0].solta_ingrediente(True, self.Pizza)
                                    self.trava = 0
                                else:
                                    self.erroIngrediente +=1
                                    self.Hand[0].solta_ingrediente()

                            else:
                                self.Hand[0].solta_ingrediente()
                                self.Hand[0].i = 0 
                                self.erroIngrediente +=1

        if (Fase.jogo == "esteira") & (Fase.movimentacao_automatica == True) & (Fase.segurar_ao_clicar == False): #FASE 1
            Objeto = [None]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT) & (self.colisao_ingrediente(Objeto,self.Hand[0])):
                        self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                        Objeto[0].pega_ingrediente(self.Pizza)
                    if self.colisao_mao(self.receita,self.Hand[0]):
                        self.receita.abre_Receita()
                    if (event.key == pygame.K_RIGHT) & (self.colisao_ingrediente(Objeto,self.Hand[1])):
                        self.Hand[1].pega_ingrediente(Objeto[0],self.Pizza)
                        Objeto[0].pega_ingrediente(self.Pizza)
                    if self.colisao_mao(self.receita,self.Hand[1]):
                        self.receita.abre_Receita()
            if self.Hand[0].pegou:
                if self.trava >= 20:
                    if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                        if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                            Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                            self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                            self.Hand[0].solta_ingrediente(True, self.Pizza)
                            self.trava = 0
                        else:
                             self.Hand[0].solta_ingrediente_esteira()
                             self.Hand[0].i = 0  # !!!
                             self.erroIngrediente +=1
                    else:
                        self.Hand[0].solta_ingrediente_esteira()
                        self.Hand[0].i = 0  # !!!
                        self.erroIngrediente +=1
                else:                   
                    self.trava +=1

            if self.Hand[1].pegou:
                if self.trava >= 20:
                    if self.Pizza.rect.colliderect(self.Hand[1].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                        if self.Hand[1].ingrediente.ingrediente in Fase.listaPizza[0]:
                            Fase.listaPizza[0].remove(self.Hand[1].ingrediente.ingrediente)
                            self.Pizza.solta_ingrediente(self.Hand[1].ingrediente)
                            self.Hand[1].solta_ingrediente_esteira(True, self.Pizza)
                            self.trava = 0
                        else:
                             self.Hand[1].solta_ingrediente_esteira()
                             self.Hand[1].i = 0  # !!!
                             self.erroIngrediente +=1

                    else:
                        self.Hand[1].solta_ingrediente_esteira()
                        self.Hand[1].i = 0  # !!!
                        self.erroIngrediente +=1
                else:                   
                    self.trava +=1


    
        if (Fase.jogo == "esteira") & (Fase.movimentacao_automatica == True) & (Fase.segurar_ao_clicar == True): #FASE 2
            Objeto = [None]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT) & (self.colisao_ingrediente(Objeto,self.Hand[0])):
                        self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                        Objeto[0].pega_ingrediente(self.Pizza)
                    if self.colisao_mao(self.receita,self.Hand[0]):
                        self.receita.abre_Receita()
                    if (event.key == pygame.K_RIGHT) & (self.colisao_ingrediente(Objeto,self.Hand[1])):
                        self.Hand[1].pega_ingrediente(Objeto[0],self.Pizza)
                        Objeto[0].pega_ingrediente(self.Pizza)
                    if self.colisao_mao(self.receita,self.Hand[1]):
                        self.receita.abre_Receita()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if self.Hand[0].pegou:
                            self.Hand[0].pegou = False
                            if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                                if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                                    Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                                    self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                                    self.Hand[0].solta_ingrediente_esteira(True, self.Pizza)
                                    self.trava = 0
                                else:
                                     self.Hand[0].solta_ingrediente_esteira()
                                     self.Hand[0].i = 0  # !!!
                                     self.erroIngrediente +=1
                            else:
                                self.Hand[0].solta_ingrediente_esteira()
                                self.Hand[0].i = 0  # !!!
                                self.erroIngrediente +=1

                    if event.key == pygame.K_RIGHT:
                        if self.Hand[1].pegou:
                            self.Hand[1].pegou = False
                            if self.Pizza.rect.colliderect(self.Hand[1].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                                if self.Hand[1].ingrediente.ingrediente in Fase.listaPizza[0]:
                                    Fase.listaPizza[0].remove(self.Hand[1].ingrediente.ingrediente)
                                    self.Pizza.solta_ingrediente(self.Hand[1].ingrediente)
                                    self.Hand[1].solta_ingrediente_esteira(True, self.Pizza)
                                    self.trava = 0
                                else:
                                     self.Hand[1].solta_ingrediente_esteira()
                                     self.Hand[1].i = 0  # !!!
                                     self.erroIngrediente +=1

                            else:
                                self.Hand[1].solta_ingrediente_esteira()
                                self.Hand[1].i = 0  # !!!
                                self.erroIngrediente +=1

    def checa_eventos_push(self,Fase):
        Objeto = [None]
        self.delay += 1
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)  # Define pinagem física (outra opção BCM)

        GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


       #if (GPIO.input(40) == 1) & (self.delay > self.trava):
       #    self.Hand.move("LEFT", "DOWN", self.size)
       #    self.trava = self.delay
       #    self.entrou = True
       #
       #if (GPIO.input(8) == 1) & (self.delay > self.trava):
       #    self.Hand.move("RIGHT", "DOWN", self.size)
       #    self.trava = self.delay
       #    self.entrou = True

       #if (GPIO.input(10) == 1) & (self.delay > self.trava):
       #    self.segurando = True
       #    if self.colisao_ingrediente(Objeto):
       #        self.Hand.pega_ingrediente(Objeto,self.Pizza)
       #        self.Hand.pegou = True
       #        self.Hand.ingrediente = Objeto[0]

      # if self.Hand.pegou & (self.segurando == False):
      #     self.Hand.pegou = False
      #     if self.Pizza.rect.colliderect(self.Hand.rect):
      #         self.Pizza.solta_ingrediente(self.Hand.ingrediente)
      #         self.Hand.solta_ingrediente()
      #
      #     else:
      #         self.Hand.solta_ingrediente()
      #
      # if (self.delay > self.trava) & (self.entrou == True) & (self.segurando == False):
      #     self.Hand.para_mao()
      #     self.entrou = False
      # self.segurando = False

        if (Fase.jogo != "esteira") & (Fase.movimentacao_automatica == True)  & (Fase.segurar_ao_clicar == False): #FASE 1
            Objeto = [None]
            if self.Hand[0].pegou == False:
                if (self.Hand[0].rect.x <= self.DISPLAY_W - self.Hand[0].retorna_largura_imagem_mao()) & (self.mov == "D"):
                    self.Hand[0].move("RIGHT", "DOWN", self.size)
                elif (self.Hand[0].rect.x >= self.DISPLAY_W - self.Hand[0].retorna_largura_imagem_mao())  & (self.mov == "D"):
                    self.mov = "E"
                    self.Hand[0].movex = 0
                elif (self.Hand[0].rect.x >= 0) & (self.mov == "E"):
                    self.Hand[0].move("LEFT", "DOWN", self.size)
                    self.mov = "E"
                elif self.Hand[0].rect.x <= 0 & (self.mov == "E"):
                    self.mov = "D"
                    self.Hand[0].movex = 0
            if self.Hand[0].pegou:
                if self.trava_ing >= 18:
                    if self.Pizza.rect.colliderect(self.Hand[0].rect):
                        if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                            Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                            self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                            self.Hand[0].solta_ingrediente(True, self.Pizza)
                            self.trava = 0
                        else:
                            self.erroIngrediente +=1
                            self.Hand[0].solta_ingrediente()
                else:                   
                    self.trava_ing +=1



            if (GPIO.input(10) == 1) & (self.delay > self.trava):
                print(self.delay, self.trava)
                self.segurando = True
                self.trava = self.delay
                if self.colisao_ingrediente(Objeto,self.Hand[0]):
                    #self.Hand.inix = self.Hand.movex #!!!
                    #self.Hand.iniy = self.Hand.movey #!!!
                    self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                    Objeto[0].pega_ingrediente(self.Pizza)
                if self.colisao_mao(self.receita,self.Hand[0]):
                    self.receita.abre_Receita()

#--------------------------------------------------------
        if (Fase.jogo != "esteira") & (Fase.movimentacao_automatica == True)  & (Fase.segurar_ao_clicar == True): #FASE 2
            Objeto = [None]
            if self.Hand[0].pegou == False:
                if (self.Hand[0].rect.x <= self.DISPLAY_W - self.Hand[0].retorna_largura_imagem_mao()) & (self.mov == "D"):
                    self.Hand[0].move("RIGHT", "DOWN", self.size)
                elif (self.Hand[0].rect.x >= self.DISPLAY_W - self.Hand[0].retorna_largura_imagem_mao())  & (self.mov == "D"):
                    self.mov = "E"
                    self.Hand[0].movex = 0
                elif (self.Hand[0].rect.x >= 0) & (self.mov == "E"):
                    self.Hand[0].move("LEFT", "DOWN", self.size)
                    self.mov = "E"
                elif self.Hand[0].rect.x <= 0 & (self.mov == "E"):
                    self.mov = "D"
                    self.Hand[0].movex = 0

            if (GPIO.input(10) == 1) & (self.delay > self.trava):
                self.segurando = True
                if self.colisao_ingrediente(Objeto,self.Hand[0]):
                    self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                    Objeto[0].pega_ingrediente(self.Pizza)
                if self.colisao_mao(self.receita,self.Hand[0]):
                    self.receita.abre_Receita()
            if self.Hand[0].pegou & (self.segurando == False):                
                self.Hand[0].pegou = False
                if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                    if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                        Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                        self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                        self.Hand[0].solta_ingrediente(True, self.Pizza)
                        self.trava = 0
                    else:
                        self.erroIngrediente +=1
                        self.Hand[0].solta_ingrediente()
                else:
                    self.Hand[0].solta_ingrediente()
                    self.Hand[0].i = 0 
                    self.erroMovimento +=1
        #---------------------------------------------------------
        if (Fase.jogo != "esteira") & (Fase.movimentacao_automatica == False)  & (Fase.segurar_ao_clicar == True): #FASE 3
            Objeto = [None]
            if (GPIO.input(40) == 1) & (self.delay > self.trava):
                self.Hand[0].move("LEFT", "DOWN", self.size)
                self.trava = self.delay
                self.entrou = True

            if (GPIO.input(8) == 1) & (self.delay > self.trava):
                self.Hand[0].move("RIGHT", "DOWN", self.size)
                self.trava = self.delay
                self.entrou = True
            if (GPIO.input(10) == 1) & (self.delay > self.trava):
                self.segurando = True
                if self.colisao_ingrediente(Objeto,self.Hand[0]):
                    self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                    Objeto[0].pega_ingrediente(self.Pizza)
                if self.colisao_mao(self.receita,self.Hand[0]):
                    self.receita.abre_Receita()

            if self.Hand[0].pegou & (self.segurando == False):                
                self.Hand[0].pegou = False
                if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                    if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                        Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                        self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                        self.Hand[0].solta_ingrediente(True, self.Pizza)
                        self.trava = 0
                    else:
                        self.erroIngrediente +=1
                        self.Hand[0].solta_ingrediente()
                else:
                    self.Hand[0].solta_ingrediente()
                    self.Hand[0].i = 0 
                    self.erroMovimento +=1

#-----------------------------------------------------------
        if (Fase.jogo == "esteira") & (Fase.movimentacao_automatica == True) & (Fase.segurar_ao_clicar == False): #FASE 1
            Objeto = [None]
            if (GPIO.input(40) == 1) & (self.delay_e > self.trava_e) & (self.colisao_ingrediente(Objeto,self.Hand[0])):
                self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                Objeto[0].pega_ingrediente(self.Pizza)
                self.trava_e = self.delay_e
                self.entrou = True
                if self.colisao_mao(self.receita,self.Hand[0]):
                    self.receita.abre_Receita()   
                   
            if (GPIO.input(8) == 1) & (self.delay_d > self.trava_d) & (self.colisao_ingrediente(Objeto,self.Hand[1])):
                self.trava_d = self.delay_d
                self.entrou = True
                self.Hand[1].pega_ingrediente(Objeto[0],self.Pizza)
                Objeto[0].pega_ingrediente(self.Pizza)
                if self.colisao_mao(self.receita,self.Hand[1]):
                    self.receita.abre_Receita()


            if self.Hand[0].pegou:
                if self.trava >= 20:
                    if self.Pizza.rect.colliderect(self.Hand[0].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                        if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                            Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                            self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                            self.Hand[0].solta_ingrediente(True, self.Pizza)
                            self.trava = 0
                        else:
                             self.Hand[0].solta_ingrediente_esteira()
                             self.Hand[0].i = 0  # !!!
                             self.erroIngrediente +=1
                    else:
                        self.Hand[0].solta_ingrediente_esteira()
                        self.Hand[0].i = 0  # !!!
                        self.erroIngrediente +=1
                else:                   
                    self.trava +=1

            if self.Hand[1].pegou:
                if self.trava >= 20:
                    if self.Pizza.rect.colliderect(self.Hand[1].rect) & self.colisao_ingrediente(Objeto,self.Hand[0]):
                        if self.Hand[1].ingrediente.ingrediente in Fase.listaPizza[0]:
                            Fase.listaPizza[0].remove(self.Hand[1].ingrediente.ingrediente)
                            self.Pizza.solta_ingrediente(self.Hand[1].ingrediente)
                            self.Hand[1].solta_ingrediente_esteira(True, self.Pizza)
                            self.trava = 0
                        else:
                             self.Hand[1].solta_ingrediente_esteira()
                             self.Hand[1].i = 0  # !!!
                             self.erroIngrediente +=1

                    else:
                        self.Hand[1].solta_ingrediente_esteira()
                        self.Hand[1].i = 0  # !!!
                        self.erroMovimento +=1
                else:                   
                    self.trava +=1
#------------------------------------------------------------
        if (Fase.jogo == "esteira") & (Fase.movimentacao_automatica == True) & (Fase.segurar_ao_clicar == True): #FASE 2
            Objeto = [None]

            if (GPIO.input(40) == 1) & (self.delay_e > self.trava_e) & (self.colisao_ingrediente(Objeto,self.Hand[0])):
                self.Hand[0].pega_ingrediente(Objeto[0],self.Pizza)
                Objeto[0].pega_ingrediente(self.Pizza)

            if self.colisao_mao(self.receita,self.Hand[0]):
               self.receita.abre_Receita()

            if (GPIO.input(8) == 1) & (self.delay_d > self.trava_d) & (self.colisao_ingrediente(Objeto,self.Hand[1])):
               self.Hand[1].pega_ingrediente(Objeto[0],self.Pizza)
               Objeto[0].pega_ingrediente(self.Pizza)
            if self.colisao_mao(self.receita,self.Hand[1]):
               self.receita.abre_Receita()

            if self.Hand[0].pegou & (self.segurando == False):
                self.Hand[0].pegou = False
                if self.Pizza.rect.colliderect(self.Hand[0].rect):
                    if self.Hand[0].ingrediente.ingrediente in Fase.listaPizza[0]:
                        Fase.listaPizza[0].remove(self.Hand[0].ingrediente.ingrediente)
                        self.Pizza.solta_ingrediente(self.Hand[0].ingrediente)
                        self.Hand[0].solta_ingrediente_esteira(True, self.Pizza)
                        self.trava = 0
                    else:
                         self.Hand[0].solta_ingrediente_esteira()
                         self.Hand[0].i = 0  # !!!
                         self.erroIngrediente +=1
                else:
                    self.Hand[0].solta_ingrediente_esteira()
                    self.Hand[0].i = 0  # !!!
                    self.erroMovimento +=1


            if self.Hand[1].pegou & (self.segurando == False):
                self.Hand[1].pegou = False
                if self.Hand[1].ingrediente.ingrediente in Fase.listaPizza[0]:
                    Fase.listaPizza[0].remove(self.Hand[1].ingrediente.ingrediente)
                    self.Pizza.solta_ingrediente(self.Hand[1].ingrediente)
                    self.Hand[1].solta_ingrediente_esteira(True, self.Pizza)
                    self.trava = 0
                else:
                    self.Hand[1].solta_ingrediente_esteira()
                    self.Hand[1].i = 0  # !!!
                    self.erroIngrediente +=1
            else:
                self.Hand[1].solta_ingrediente_esteira()
                self.Hand[1].i = 0  # !!!
                self.erroMovimento +=1

#------------------------------------------------------------




    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def update_ingredientes(self):
        self.screen.blit(self.receita.image,self.receita.rect)
        self.receita.update()
        for i in (self.lista_ingredientes):
            # i.move(2)
            i.update()
            self.screen.blit(i.image, i.rect)
            
    def cria_igredientes(self,Fase):
        from ClsIngrediente import Ingrediente
        from ClsReceita import Receita
        if Fase.jogo == "esteira":
            if self.contador % 1000 == 0:
                lado = random.randint(0,1)
                if lado == 0:
                    self.receita = Receita([155,50])
                    ingrediente = Ingrediente([self.DISPLAY_W/1.2,50], random.randint(1,8))
                    ingrediente.control(0,2)
                    self.receita.control(0,2)
                    self.lista_ingredientes.append(ingrediente)
                else:
                    self.receita = Receita([self.DISPLAY_W/1.2+5,50])
                    ingrediente = Ingrediente([150,50], random.randint(1,8))
                    ingrediente.control(0,2)
                    self.receita.control(0,2)
                    self.lista_ingredientes.append(ingrediente)

            elif self.contador % 100 == 0:
                ingrediente = Ingrediente([150,50], random.randint(1,8))
                self.lista_ingredientes.append(ingrediente)
                ingrediente.control(0,2)
                ingrediente = Ingrediente([self.DISPLAY_W/1.2,50], random.randint(1,8))
                ingrediente.control(0,2)
                self.lista_ingredientes.append(ingrediente)

        else:
            lado = 0
            direita = 50
            esquerda = 50
            qtdingredientes = len(Fase.lista_ingredientes) +1
            self.receita = Receita([self.DISPLAY_W /1.2  ,self.DISPLAY_H/1.4])
            for ingrediente_pizza in Fase.lista_ingredientes:
                if lado == 0:
                    self.lista_ingredientes.append(Ingrediente([(self.DISPLAY_W / 2.5) - esquerda ,self.DISPLAY_H/1.4],ingrediente_pizza[0]))
                    esquerda += 120
                    lado = 1
                else:
                    self.lista_ingredientes.append(Ingrediente([(self.DISPLAY_W / 2.5) + direita ,self.DISPLAY_H/1.4],ingrediente_pizza[0]))
                    direita += 120
                    lado = 0
            
                qtdingredientes -=1
        self.contador += 1

   

    def calculo_velocidade_direcao_pizza(pizza, objeto):
       Vx = (pizza.rect.centerx  - objeto.rect.x) * -30 / (pizza.rect.centery - objeto.rect.y - pizza.retorna_altura_imagem_pizza())
       return Vx

    def cria_objetos(self,Fase):
        #self.Hand = Hand([self.DISPLAY_H/10,self.DISPLAY_W/1.5])
        #self.Hand.pizzaCenter = self.Pizza.rect.center
        #self.cria_igredientes(Fase)
        self.cria_pizza(Fase)
        self.cria_maos(Fase)

    def cria_pizza(self,ObjFase):
        from ClsPizza import Pizza
        if ObjFase.jogo == "esteira":
            self.Pizza = Pizza([(self.DISPLAY_W / 2), (300)])
        else:
            self.Pizza = Pizza([(self.DISPLAY_W / 2), (self.DISPLAY_W * 1/6)])

    def cria_maos(self,ObjFase):
       from ClsHand import Hand
       for localizacao in ObjFase.localizacao_mao:
            self.Hand.append(Hand([self.DISPLAY_W/localizacao[0],self.DISPLAY_H/localizacao[1]]))
       if ObjFase.jogo == "esteira":
            self.Hand[1].image = pygame.transform.flip(self.Hand[1].image, True, False)


    def atualiza_objetos(self,Fase):
        self.atualiza_maos(Fase)
        if Fase.jogo == "esteira":
            self.cria_igredientes(Fase)


    def atualiza_maos(self,Fase):
        for mao in self.Hand:
            mao.update()

    def blit_text(self,surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def desenha_tela(self, fase):
        #self.screen.fill(self.black)
        self.screen.blit(fase.fundo, (0, 0))
        self.screen.blit(self.Pizza.image, self.Pizza.rect)
        self.update_ingredientes()
        if (self.receita.aberta == True) or (round(fase.timescore/self.frame) < 5):
            self.desenha_receita(fase)
        self.desenha_score(fase)
        for mao in self.Hand:
            self.screen.blit(mao.image, mao.rect)
    
    def desenha_receita(self, fase):
        self.texto ="\nFase " + str(fase.dificuldade)
        self.texto =  self.texto + "\n\n" + "Receita\n"
        for ingredientes in fase.listaPizza[0]:
            self.texto = self.texto + "\n" + ingredientes[1]
        if fase.jogo == "esteira":
            self.blit_text(self.screen, self.texto, (600, 500), self.fonte)    
        else:
            self.blit_text(self.screen, self.texto, (120, 40), self.fonte)    
        self.texto = ""

    def desenha_score(self,fase):
        self.score ="Fase " + str(fase.dificuldade)
        self.score = self.score +"\nTempo " + str(round(fase.timescore/self.frame))
        self.score = self.score + "\n Erros:" + str(self.erroIngrediente)
        if fase.jogo =="esteira":
            self.blit_text(self.screen, self.score, (600, 30), self.fonteScore)
        else:
            self.blit_text(self.screen, self.score, (1050, 40), self.fonteScore)


    def checa_fase(self,fase):
        from ClsFase import Fase
        from ClsArquivo import Arquivo
        if len(fase.listaPizza[0]) == 0:
            fase.listaPizza.pop(0)
            self.lista_ingredientes = []
            self.cria_igredientes(fase)

        if len(fase.listaPizza) == 0:
            #fase = Fase(fase.dificuldade+1,fase.jogo)
            Arquivo.gera_arquivo(self.usuario,fase.jogo,fase.dificuldade,self.erroIngrediente,self.erroMovimento,str(round(fase.timescore/self.frame)))
            self.limpa_objetos()
            self.in_game_loop(fase.jogo,fase.dificuldade+1)

    def limpa_objetos(self):
        self.lista_ingredientes = []
        self.Hand = []
        self.erroIngrediente = 0
        self.receita.tempo = 0

    def in_game_loop(self,jogo,fase):
        from ClsFase import Fase
        ObjFase = Fase(jogo,fase)
        self.cria_igredientes(ObjFase)
        self.cria_objetos(ObjFase)
        contador =0

        #pygame.mixer.music.load("./images/background.mp3")
        #pygame.mixer.music.play()

        while 1: #!!! QUEBRAR QUANDO FASE ACABAR
            self.clock.tick(self.frame)
            ObjFase.timescore +=1

            self.checa_eventos_teclado(ObjFase)
            #self.checa_eventos_push(ObjFase)

            # atualiza os objetos
            self.atualiza_objetos(ObjFase)
            #self.Hand.update()
            self.desenha_tela(ObjFase)
            self.checa_fase(ObjFase)
            pygame.display.flip()

