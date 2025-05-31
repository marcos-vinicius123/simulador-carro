import pygame as pg
import src.config as config

class Camera:
    def __init__(self, x=0, y=0) -> int:
        self.pos = pg.Vector2(x, y)

    
    def seguir(self, pos):
        self.pos.x = pos.x-config.TELA_TAMANHO[0]//2
        self.pos.y = pos.y-config.TELA_TAMANHO[1]//2