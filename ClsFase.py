import random
import pygame
from ClsIngrediente import Ingrediente
class Fase():
    def __init__(self, jogo,dificuldade):
        self.Fase_Pizza_Ingredientes = [3], [2, 5], [3, 5], [4,5]
        self.listaPizza = []
        self.lista_ingredientes = [(0, "massa")]
        self.movimentacao_automatica = None
        self.localizacao_mao = []
        self.localizacao_ingredientes = []
        self.segurar_ao_clicar = None
        self.contador = None
        self.jogo = ""
        self.dificuldade = dificuldade
        self.jogo = jogo
        self.timescore =0
        self.fundo = ""
        self.setDifiuldade(jogo)



    def remove_ingredientes_repetidos(self, lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)
        l.sort()
        return l

    def retornaPizza(self,numero_ingredientes):
        pizzaRandom = [(0, "massa")]
        lista_ingredientes = random.sample(Ingrediente.ingredientes[1:len(Ingrediente.ingredientes)],len(Ingrediente.ingredientes) - 1 )
        for i in range(0, numero_ingredientes, 1):
            pizzaRandom.append(lista_ingredientes[i])
            self.lista_ingredientes.append(lista_ingredientes[i])
        self.lista_ingredientes= self.remove_ingredientes_repetidos(self.lista_ingredientes)
        return self.remove_ingredientes_repetidos(pizzaRandom)

    def setListaPizza(self,pedido):
        for pizza in pedido:
            self.listaPizza.append(self.retornaPizza(pizza))

    def setDifiuldade(self, jogo):
        if jogo != "esteira":
            self.fundo = pygame.image.load("images\Cenario1.png")
            self.localizacao_ingredientes = []
            self.localizacao_mao.append([10,1.4])
            if self.dificuldade == 1:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade-1])
                self.movimentacao_automatica = True
                self.segurar_ao_clicar = False
            elif self.dificuldade == 2:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade-1])
                self.movimentacao_automatica = True
                self.segurar_ao_clicar = True
            elif self.dificuldade == 3:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade-1])
                self.movimentacao_automatica = False
                self.segurar_ao_clicar = True
            elif self.dificuldade == 4:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade-1])
                self.movimentacao_automatica = False
                self.segurar_ao_clicar = True
                self.contador = 5000
        else:
            self.localizacao_ingredientes = []
            self.localizacao_mao.append([8,1.2])
            self.localizacao_mao.append([1.2,1.2])
            self.fundo = pygame.image.load("images\FaseEsteira.png")
            if self.dificuldade == 1:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade-1])
                self.movimentacao_automatica = True
                self.segurar_ao_clicar = False
            elif self.dificuldade == 2:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade-1])
                self.movimentacao_automatica = True
                self.segurar_ao_clicar = True
            elif self.dificuldade == 3:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade-1])
                self.movimentacao_automatica = False
                self.segurar_ao_clicar = True
            elif self.dificuldade == 4:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade-1])
                self.movimentacao_automatica = False
                self.segurar_ao_clicar = True
                self.contador = 5000

