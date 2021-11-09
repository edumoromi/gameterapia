import pygame
import inspect
#INSIDE OF THE GAME LOOP
import os; print(os.getcwd()) # mostra o diretorio atual
current_path = os.path.dirname(__file__) # Where your .py file is located
image_path = os.path.join(current_path, 'images') # The image folder path

#REST OF ITEMS ARE BLIT'D TO SCREEN.
class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        self.jogar = pygame.image.load(os.path.join(image_path, 'jogarSelecionado.png'))
        self.options = pygame.image.load(os.path.join(image_path,'options.png'))
        self.sair = pygame.image.load(os.path.join(image_path, 'sair.png'))
        self.Fundo = pygame.image.load(os.path.join(image_path, 'Fundo.jpg'))



    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        if isinstance(self,MainMenu):
            pygame.draw.rect(self.screen, self.color, self.input_box, 2) 
            txt_surface = self.font.render(self.text, True, self.color)
            width = max(200, txt_surface.get_width()+10)
            self.input_box.w = width
            self.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))

        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w - 200, self.mid_h - 80
        self.optionsx, self.optionsy = self.mid_w - 200, self.mid_h + 20
        self.creditsx, self.creditsy = self.mid_w - 200, self.mid_h + 120
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.input_box = pygame.Rect(200, 100, 140, 32)
        self.screen = pygame.display.set_mode((self.game.DISPLAY_W,  self.game.DISPLAY_H))
        #COLORS
        self.font = pygame.font.Font(None, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = pygame.Color('black')
        self.active = False
        self.text = ''
        self.done = False

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.blit(self.Fundo, (0, 0))
            #self.check_events()
            self.game.check_events(self)
            #self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.display.blit(self.jogar, (self.startx, self.starty))
            self.game.display.blit(self.options, (self.optionsx, self.optionsy))
            self.game.display.blit(self.sair,(self.creditsx, self.creditsy))
            self.check_input()
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.jogar = pygame.image.load("images\jogar.png")
                self.options = pygame.image.load("images\optionsSelecionado.png")
                self.sair = pygame.image.load("images\sair.png")
                self.state = 'Options'
            elif self.state == 'Options':
                self.jogar = pygame.image.load("images\jogar.png")
                self.options = pygame.image.load("images\options.png")
                self.sair = pygame.image.load("images\sairSelecionado.png")
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.jogar = pygame.image.load("images\jogarSelecionado.png")
                self.options = pygame.image.load("images\options.png")
                self.sair = pygame.image.load("images\sair.png")
                self.state = 'Start'

        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.jogar = pygame.image.load("images\jogar.png")
                self.options = pygame.image.load("images\options.png")
                self.sair = pygame.image.load("images\sairSelecionado.png")
                #self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.jogar = pygame.image.load("images\jogarSelecionado.png")
                self.options = pygame.image.load("images\options.png")
                self.sair = pygame.image.load("images\sair.png")
                self.state = 'Start'
            elif self.state == 'Credits':
                self.jogar = pygame.image.load("images\jogar.png")
                self.options = pygame.image.load("images\optionsSelecionado.png")
                self.sair = pygame.image.load("images\sair.png")
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.usuario = self.text 
                self.game.playing = True
                
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()


