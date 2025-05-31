import pygame as pg
import random
import src.config as config
from src.carro import Carro

class Evolutivo:
    def __init__(self, pos_inicial):
        self.pos_inicial = pos_inicial
        self.carros = []
        self.gerar_geracao_inicial()
    
    def update(self, fundo):
        for carro in  self.carros:
            carro.update(fundo)

    def render(self, tela, camera):
        for carro in self.get_melhores(config.GERACAO_CARROS_SIZE):
            carro.render(tela, camera)
    
    def get_melhores(self, quantidade):
        return sorted(self.carros, key=self.calcular_fitness)[0:quantidade]
    
    def calcular_fitness(self, carro):
        return carro.roda1.y
    
    def gerar_geracao_inicial(self):
        self.carros = []
        for i in range(config.GERACAO_CARROS_SIZE):
            constantes = [random.randint(0, 1000)/10000 for _ in range(3)]
            self.carros.append(Carro(self.pos_inicial.x, self.pos_inicial.y, *constantes))