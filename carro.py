import pygame as pg
import math
import config

class Carro:
    def __init__(self, x, y):
        self.pos = pg.Vector2(x, y)
        self.angulo = 0
        self.roda1 = pg.Vector2(x-30, y)
        self.roda2 = pg.Vector2(x+30, y)
    
    def update(self, roda_esquerda, roda_direita):
        roda1 = pg.Vector2(self.roda1.x, self.roda1.y)
        roda2 = pg.Vector2(self.roda2.x, self.roda2.y)

        if roda_esquerda:
            self.angulo += 0.25 
            self.roda1.x = self.roda2.x - 60 * math.cos(self.angulo)
            self.roda1.y = self.roda2.y - 60 * math.sin(self.angulo)

            self.roda2.x = self.roda1.x + 60 * math.cos(self.angulo)
            self.roda2.y = self.roda1.y + 60 * math.sin(self.angulo)
        
        if roda_direita:
            self.angulo -= 0.25
            self.roda2.x = self.roda1.x + 60 * math.cos(self.angulo)
            self.roda2.y = self.roda1.y + 60 * math.sin(self.angulo)

            self.roda1.x = self.roda2.x - 60 * math.cos(self.angulo)
            self.roda1.y = self.roda2.y - 60 * math.sin(self.angulo)


    def render(self, tela):
        pg.draw.line(tela, (100, 120, 100), (self.roda1.x, self.roda1.y), (self.roda2.x, self.roda2.y))
        pg.draw.circle(tela, (120, 100, 100), (self.roda1.x, self.roda1.y), 5)
        pg.draw.circle(tela, (120, 100, 100), (self.roda2.x, self.roda2.y), 5)
