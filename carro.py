import pygame as pg
import math
import config

class Carro:
    def __init__(self, x, y):
        self.pos = pg.Vector2(x, y)
        self.angulo = 0
        self.roda1 = pg.Vector2(x-30, y)
        self.vel1 = 0.1
        self.roda2 = pg.Vector2(x+30, y)
        self.vel2 = 0.1
        self.sensores = [False for _ in range(8)]
    
    def update(self, roda_esquerda, roda_direita, tela):
        roda1 = pg.Vector2(self.roda1.x, self.roda1.y)
        roda2 = pg.Vector2(self.roda2.x, self.roda2.y)

        if roda_esquerda:
            self.angulo += self.vel1 
            self.roda1.x = self.roda2.x - 60 * math.cos(self.angulo)
            self.roda1.y = self.roda2.y - 60 * math.sin(self.angulo)

            self.roda2.x = self.roda1.x + 60 * math.cos(self.angulo)
            self.roda2.y = self.roda1.y + 60 * math.sin(self.angulo)
        
        if roda_direita:
            self.angulo -= self.vel2
            self.roda2.x = self.roda1.x + 60 * math.cos(self.angulo)
            self.roda2.y = self.roda1.y + 60 * math.sin(self.angulo)

            self.roda1.x = self.roda2.x - 60 * math.cos(self.angulo)
            self.roda1.y = self.roda2.y - 60 * math.sin(self.angulo)
        
        self.update_sensores(tela)

    def update_sensores(self, tela):
        for i in range(8):
            sensor_pos = pg.Vector2(self.roda1.x+(10+6*i)*math.cos(self.angulo), (self.roda1.y+(10+6*i)*math.sin(self.angulo)))
            self.sensores[i] = tuple(tela.get_at((int(sensor_pos.x), int(sensor_pos.y))))[0]!=config.COR_FUNDO[0]
            # print(tela.get_at(sensor_pos))

    def render(self, tela):
        pg.draw.line(tela, (100, 120, 100), (self.roda1.x, self.roda1.y), (self.roda2.x, self.roda2.y))
        pg.draw.circle(tela, (120, 100, 100), (self.roda1.x, self.roda1.y), 5)
        pg.draw.circle(tela, (120, 100, 100), (self.roda2.x, self.roda2.y), 5)

        for i in range(len(self.sensores)):
            pg.draw.circle(tela, (255* (not self.sensores[i]), self.sensores[i]*255, 0), (self.roda1.x+(10+6*i)*math.cos(self.angulo), (self.roda1.y+(10+6*i)*math.sin(self.angulo))), 2)
        # ir_pos = pg.Vector2(self.roda1.x, self.roda1.y)
        # for i in range(8):
        #     pg.draw.rect(tela, (0, 255, 0), (ir_pos.x, ir_pos.y, 1, 1))
        #     ir_pos.x = ir_pos.x + 6 * math.cos(self.angulo) *i
        #     ir_pos.y = ir_pos.y + 6 * math.sin(self.angulo) * 1