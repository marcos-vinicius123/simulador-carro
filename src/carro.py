import pygame as pg
import math
import src.config as config
from src.seguidor import Seguidor

class Carro:
    def __init__(self, x:int, y:int, kp:float, ki:float, kd:float):
        self.pos = pg.Vector2(x, y)
        self.angulo = 0
        self.roda1 = pg.Vector2(x-30, y)
        self.vel1 = 0.02
        self.roda2 = pg.Vector2(x+30, y)
        self.vel2 = 0.02
        self.sensores = [False for _ in range(8)]
        self.seguidor = Seguidor(kp, ki, kd)
    
    def update(self, tela:pg.Surface):
        roda1 = pg.Vector2(self.roda1.x, self.roda1.y)
        roda2 = pg.Vector2(self.roda2.x, self.roda2.y)

        self.update_sensores(tela)
        seguidor_valor = self.seguidor.rodar_seguidor(self.sensores)
        vel1 = max(0, self.vel1+seguidor_valor)
        vel2 = max(0, self.vel2-seguidor_valor)
        
        self.angulo += vel1 
        self.roda1.x = self.roda2.x - 60 * math.cos(self.angulo)
        self.roda1.y = self.roda2.y - 60 * math.sin(self.angulo)

        self.roda2.x = self.roda1.x + 60 * math.cos(self.angulo)
        self.roda2.y = self.roda1.y + 60 * math.sin(self.angulo)
  
        self.angulo -= vel2
        self.roda2.x = self.roda1.x + 60 * math.cos(self.angulo)
        self.roda2.y = self.roda1.y + 60 * math.sin(self.angulo)

        self.roda1.x = self.roda2.x - 60 * math.cos(self.angulo)
        self.roda1.y = self.roda2.y - 60 * math.sin(self.angulo)
        
        

    def update_sensores(self, fundo:pg.Surface):
        for i in range(len(self.sensores)):
            sensor_pos = pg.Vector2(self.roda1.x+(10+6*i)*math.cos(self.angulo), (self.roda1.y+(10+6*i)*math.sin(self.angulo)))
            try:
                self.sensores[i] = tuple(fundo.get_at((int(sensor_pos.x), int(sensor_pos.y))))[0]!=config.COR_FUNDO[0]
            except:
                self.sensores[i] = False
    
    def render(self, tela:pg.Surface, camera):
        pg.draw.line(tela, (100, 120, 100), (self.roda1.x-camera.pos.x, self.roda1.y-camera.pos.y), (self.roda2.x-camera.pos.x, self.roda2.y-camera.pos.y))
        pg.draw.circle(tela, (120, 100, 100), (self.roda1.x-camera.pos.x, self.roda1.y-camera.pos.y), 5)
        pg.draw.circle(tela, (120, 100, 100), (self.roda2.x-camera.pos.x, self.roda2.y-camera.pos.y), 5)

        
        for i in range(len(self.sensores)):
            pg.draw.circle(tela, (255* (not self.sensores[i]), self.sensores[i]*255, 0), (self.roda1.x+(10+6*i)*math.cos(self.angulo)-camera.pos.x, self.roda1.y+(10+6*i)*math.sin(self.angulo)-camera.pos.y), 2)