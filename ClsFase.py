import random
import pygame

class Fase():

    def __init__(self):

        self.ingredientes = ["massa", "cogumelo", "molho", "tomate", "AzeitonaPreta", "AzeitonaVerde", "queijo", "calabresa",
                             "cebola", "peixe"]

        self.pizzaRandom = ["massa"]

    def dificuldadeFase(self, dificuldade):
        random.shuffle(self.ingredientes)
        for i in range(0, dificuldade, 1):
            self.pizzaRandom.append(self.ingredientes[i])
            print(self.pizzaRandom[i])

