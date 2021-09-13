import random
import pygame
from ClsIngrediente import Ingrediente
class Fase():
    Fase_Pizza_Ingredientes = [1, 5], [2, 5], [3, 4], [4,5]
    listaPizza = []
    lista_ingredientes = []
    movimentacao_automatica = None
    localizacao_mao = []
    localizacao_ingredientes = []
    segurar_ao_clicar = None
    contador = None
    jogo = ""

    def __init__(self, dificuldade,jogo):
        self.dificuldade = dificuldade
        self.jogo = jogo
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
        lista_ingredientes = random.sample(Ingrediente.ingredientes,len(Ingrediente.ingredientes))
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
            self.localizacao_ingredientes = []
            self.localizacao_mao.append([10,1.5])
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
            self.localizacao_mao.append([8,2])
            self.localizacao_mao.append([1.3,2])
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

