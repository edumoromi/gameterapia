import pygame

from ClsImage import Image
from ClsMenu import *
from ClsIngrediente import Ingrediente
import random
import sys
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD) #Define pinagem física (outra opção BCM)

#GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(40, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
class Game():
    #Tamanho da tela do jogo.
    DISPLAY_W, DISPLAY_H = 800, 600
    lista_ingrediente = []
    size =800, 600
    screen = pygame.display.set_mode(size)
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.size = width, height = self.DISPLAY_W, self.DISPLAY_H
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        #self.font_name = '8-BIT WONDER.TTF'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing= False
            self.display.fill(self.BLACK)
            self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, (0,0))
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

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def update_ingredientes(self):
        for i in (self.lista_ingrediente):
            #i.move(2)
            i.update()
            self.screen.blit(i.image, i.rect)

    def in_game_loop(self):
        from ClsHand import Hand
        from ClsPizza import Pizza
        from ClsIngrediente import Ingrediente
        pegou = False #AJUSTAR VARIAVEL
        # ingrediente =""
        Pizza = Pizza([(self.DISPLAY_W / 2), (self.DISPLAY_W / 2)])
        Hand1 = Hand([150, self.DISPLAY_W / 2])
        Hand2 = Hand([self.DISPLAY_W/1.2, self.DISPLAY_W / 2])
        # Molho = Ingrediente([self.DISPLAY_H/1.5,self.DISPLAY_W/1.7],"MolhoTomate.png")
        # calabresa = Ingrediente([self.DISPLAY_H/2.0,self.DISPLAY_W/1.7],"calabresa.png")
        # cogumelo = Ingrediente([self.DISPLAY_H/1.2,self.DISPLAY_W/1.7],"cogumelo.png")
        # tomate = Ingrediente([self.DISPLAY_H / 3, self.DISPLAY_W / 1.7],"tomate.png")
        # massa = Ingrediente([self.DISPLAY_H/6,self.DISPLAY_W/1.7],"massa.png")
        pygame.display.set_caption('Hand!')
        clock = pygame.time.Clock()
        black = 255, 255, 255
        delay = 0
        trava = 0
        entrou = False
        segurando = False
        contador =0
        while 1:
            if contador % 200 == 0:
                ingrediente = Ingrediente([150,50], random.randint(1,8))
                self.lista_ingrediente.append(ingrediente)
                ingrediente = Ingrediente([self.DISPLAY_W/1.2,50], random.randint(1,8))
                self.lista_ingrediente.append(ingrediente)
            contador +=1
            # garante que o programa nao vai rodar a mais que 120fps
            clock.tick(120)
            delay +=1
            # checa eventos de teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if(self.colisao_ingrediente_hand1(Hand1)):
                            x = Hand1.rect.x
                            y = Hand1.rect.y
                            Hand1.image, Hand1.rect = Image.load_image("MaoFechada.png")
                            Hand1.image = pygame.transform.scale(Hand1.image, (100, 100))
                            Hand1.rect.x = x
                            Hand1.rect.y = y
                            Hand1.control(2,0)
                            pegou = True
                    if event.key == pygame.K_RIGHT:
                        if(self.colisao_ingrediente_hand2(Hand2)):
                            x = Hand2.rect.x
                            y = Hand2.rect.y
                            Hand2.image, Hand2.rect = Image.load_image("MaoFechada.png")
                            Hand2.image = pygame.transform.scale(Hand2.image, (100, 100))
                            Hand2.rect.x = x
                            Hand2.rect.y = y
                            Hand2.control(-2,0)
                            pegou = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if pegou:
                            pegou = False
                            if Pizza.rect.colliderect(Hand1.rect):
                                Hand1.para_mao()
                            else:
                                Hand1.para_mao()
                    if event.key == pygame.K_RIGHT:
                        if pegou:
                            pegou = False
                            if Pizza.rect.colliderect(Hand2.rect):
                                Hand2.para_mao()
                            else:
                                Hand2.para_mao()

            """
            if (GPIO.input(40) == 1) & (delay > trava):
                Hand.move("LEFT","DOWN",self.size)
                print("ESQUERDA")
                entrou = True
                trava = delay
            if (GPIO.input(8) == 1) & (delay > trava):
                Hand.move("RIGHT","DOWN",self.size)
                print("DIREITA")
                trava = delay
                entrou = True
            if (GPIO.input(10) == 1) & (delay > trava):
                print("MEIO")
                segurando = True
                if Hand.rect.colliderect(Molho.rect) & (ingrediente != "cogumelo"): #TA BATENDO NO MOLHO DE TOMATE AO PEGR COGUMELO
                    Hand.pega_ingrediente("molho")
                    pegou = True
                    ingrediente = "molho"
                elif Hand.rect.colliderect(massa.rect):
                    Hand.pega_ingrediente("massa")
                    pegou = True
                    ingrediente = "massa"
                elif Hand.rect.colliderect(cogumelo.rect):
                    Hand.pega_ingrediente("cogumelo")
                    pegou = True
                    ingrediente = "cogumelo"
            if pegou & (segurando == False):
                pegou = False
                if Pizza.rect.colliderect(Hand.rect):
                    Hand.solta_ingrediente()
                    Pizza.solta_ingrediente(ingrediente)
                else:
                    Hand.solta_ingrediente()
            # atualiza os  objetos
            """

            if (delay > trava) & (entrou == True) & (segurando == False):
                Hand.para_mao()
                entrou = False
            segurando = False

            self.colisao_ingrediente_hand1(Hand1)
            self.colisao_ingrediente_hand2(Hand2)

            Hand1.update()
            Hand2.update()
            # atualiza os objetos
            # redesenha a tela
            self.screen.fill(black)
            self.screen.blit(Pizza.image, Pizza.rect)
            self.update_ingredientes()
            self.screen.blit(Hand1.image, Hand1.rect)
            self.screen.blit(Hand2.image, Hand2.rect)

            pygame.display.flip()

    def colisao_ingrediente_hand1(self,HAND1):
        for i in (self.lista_ingrediente):
            if HAND1.rect.colliderect(i.rect):
                return True
            return False

    def colisao_ingrediente_hand2(self,HAND2):
        for i in (self.lista_ingrediente):
            if HAND2.rect.colliderect(i.rect):
                return True
        return False