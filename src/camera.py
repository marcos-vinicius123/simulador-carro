import pygame as pg
import src.config as config

class Camera:
    def __init__(self, x=0, y=0) -> int:
        self.pos = pg.Vector2(x, y)

    
    def seguir(self, pos, fundo):
        self.pos.x = pos.x-config.TELA_TAMANHO[0]//2
        self.pos.y = pos.y-config.TELA_TAMANHO[1]//2
        self.constrain(fundo)
    
    def mover(self, x, y, fundo):
        self.pos.x += x
        self.pos.y += y
        self.constrain(fundo)

    def constrain(self, fundo):
        if self.pos.x<0:
            self.pos.x = 0
        
        elif self.pos.x+config.TELA_TAMANHO[0]>fundo.get_width():
            self.pos.x = fundo.get_width()-config.TELA_TAMANHO[0]

        
        if self.pos.y<0:
            self.pos.y = 0
        
        elif self.pos.y+config.TELA_TAMANHO[1]>fundo.get_height():
            self.pos.y = fundo.get_height()-config.TELA_TAMANHO[1]