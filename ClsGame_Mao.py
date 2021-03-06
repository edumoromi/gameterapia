import pygame
from ClsMenu import *
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) #Define pinagem física (outra opção BCM)

GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
class Game():
    #Tamanho da tela do jogo.
    DISPLAY_W, DISPLAY_H = 800, 600

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

    def in_game_loop(self):
        from ClsHand import Hand
        from ClsPizza import Pizza
        from ClsIngrediente import Ingrediente
        pegou = False #AJUSTAR VARIAVEL
        ingrediente =""
        Pizza = Pizza([(self.DISPLAY_W / 1.9), (self.DISPLAY_W * 1/6)])
        Hand = Hand([self.DISPLAY_H/10,self.DISPLAY_W/1.5])
        Molho = Ingrediente([self.DISPLAY_H/1.5,self.DISPLAY_W/1.7],"MolhoTomate.png")
        calabresa = Ingrediente([self.DISPLAY_H/2.0,self.DISPLAY_W/1.7],"calabresa.png")
        cogumelo = Ingrediente([self.DISPLAY_H/1.2,self.DISPLAY_W/1.7],"cogumelo.png")
        tomate = Ingrediente([self.DISPLAY_H / 3, self.DISPLAY_W / 1.7],"tomate.png")
        massa = Ingrediente([self.DISPLAY_H/6,self.DISPLAY_W/1.7],"massa.png")
        pygame.display.set_caption('Hand!')
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.size)
        black = 255, 255, 255
        delay = 0
        trava = 0
        entrou = False
        segurando = False
        while 1:
            # garante que o programa nao vai rodar a mais que 120fps
            clock.tick(120)
            delay +=1
            # checa eventos de teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Hand.move("LEFT","DOWN",self.size)
                    if event.key == pygame.K_RIGHT:
                        Hand.move("RIGHT","DOWN",self.size)
                    if event.key == pygame.K_SPACE:
                        if Hand.rect.colliderect(Molho.rect):
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
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        Hand.move("LEFT","UP",self.size)
                    if event.key == pygame.K_RIGHT:
                        Hand.move("RIGHT","UP",self.size)
                    if event.key == pygame.K_SPACE:
                        if pegou:
                            pegou = False
                            if Pizza.rect.colliderect(Hand.rect):
                                Hand.solta_ingrediente()
                                Pizza.solta_ingrediente(ingrediente)
                            else:
                                Hand.solta_ingrediente()
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
            print("velocidade:"+ str(Hand.velocidade_x))
            if (delay > trava) & (entrou == True) & (segurando == False):
                Hand.para_mao()
                entrou = False
            segurando = False
            Hand.update()
            # atualiza os objetos
            Hand.update()
            print(ingrediente)
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