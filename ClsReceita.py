import pygame

import random

from ClsImage import Image
from ClsGame import Game



class Receita(pygame.sprite.Sprite):
    def __init__(self, startpos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Image.load_image("receita.png")
        #self.image = pygame.transform.scale(self.image,(50,50)) #Muda o tamanho da imagem !!! ERRO DE COLISAO
        #self.Receita = self.Receitas[image]
        self.rect.x = startpos[0]
        self.rect.y = startpos[1]
        self.init_pos = startpos
        self.movex = 0
        self.movey = 0
        self.tempo = 0
        self.aberta = False

    def control(self, x, y):
        self.movex += x
        self.movey += y
        
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        if (self.aberta == True) & (self.tempo < 100):
            self.tempo +=1
        elif (self.aberta == True):
            self.fecha_Receita()

    def pega_Receita(self,pizza): #AJUSTAR FUNCAO
        self.control(float(Game.calculo_velocidade_direcao_pizza(pizza,self)),-20)
    
    def solta_Receita(self):
        self.movex = 0
        self.movey = 0
    
    def abre_Receita(self):
        if self.aberta == False:
            x = self.rect.x 
            y = self.rect.y 
            self.image, self.rect = Image.load_image("receita_aberta.png")
            self.rect.x = x - 30
            self.rect.y = y
            self.aberta = True

    def fecha_Receita(self):
        x = self.rect.x 
        y = self.rect.y 
        self.image, self.rect = Image.load_image("receita.png")
        self.rect.x = x + 30
        self.rect.y = y
        self.aberta = False
        self.tempo = 0


