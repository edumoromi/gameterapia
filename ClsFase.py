import random
import pygame
from ClsIngrediente import Ingrediente
class Fase():
    Fase_Pizza_Ingredientes = [1, 5], [2, 5], [3, 4]
    movimentacao_automatica = None
    segurar_ao_clicar = None
    contador = None

    def __init__(self, dificuldade):
        self.dificuldade = dificuldade
        self.setDifiuldade()

    def retornaPizza(self,numero_ingredientes):
        pizzaRandom = ["massa"]
        lista_ingredientes = random.shuffle(Ingrediente.ingredientes)
        for i in range(0, numero_ingredientes, 1):
            pizzaRandom.append(lista_ingredientes[i])
            return pizzaRandom

    def setListaPizza(self,pedido):
        for pizza in pedido:
            self.listaPizza.append(self.retornaPizza(pizza))

    def setDifiuldade(self, jogo):
        if jogo != "esteira":
            if self.dificuldade == 1:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade])
                self.movimentacao_automatica = True
                self.segurar_ao_clicar = False
            elif self.dificuldade == 2:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade])
                self.movimentacao_automatica = True
                self.segurar_ao_clicar = True
            elif self.dificuldade == 3:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade])
                self.movimentacao_automatica = False
                self.segurar_ao_clicar = True
            elif self.dificuldade == 4:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade])
                self.movimentacao_automatica = False
                self.segurar_ao_clicar = True
                self.contador = 5000
        else:
            if self.dificuldade == 1:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade])
                self.movimentacao_automatica = True
                self.segurar_ao_clicar = False
            elif self.dificuldade == 2:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade])
                self.movimentacao_automatica = True
                self.segurar_ao_clicar = True
            elif self.dificuldade == 3:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade])
                self.movimentacao_automatica = False
                self.segurar_ao_clicar = True
            elif self.dificuldade == 4:
                self.setListaPizza(self.Fase_Pizza_Ingredientes[self.dificuldade])
                self.movimentacao_automatica = False
                self.segurar_ao_clicar = True
                self.contador = 5000

