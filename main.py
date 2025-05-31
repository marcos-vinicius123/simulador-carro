import pygame as pg
import math
import src.config as config
from src.carro import Carro
from src.camera import Camera

pg.init()

def main():
    tela = pg.display.set_mode(config.TELA_TAMANHO)
    clock = pg.time.Clock()
    fonte = pg.font.SysFont("Calibri", 16)
    rodando = True
    pausado = True
    debug = False
    carro = None
    movendo_camera = False
    camera =  Camera(0, 0)

    fundo_img = pg.image.load("imgs/fundo_imenso.png").convert()
    pausado_img = fonte.render("pausado", False, (255, 0, 0))

    while rodando:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                rodando = False
                return
        
            elif e.type==pg.KEYUP:
                if e.key==pg.K_SPACE and carro:
                    pausado =  not pausado
                elif e.key==pg.K_1:
                    debug = not debug

            elif e.type==pg.MOUSEBUTTONUP:
                if e.button==3:
                    mouse_pos = pg.mouse.get_pos()
                    carro = Carro(mouse_pos[0]+camera.pos.x, mouse_pos[1]+camera.pos.y)

            elif e.type==pg.MOUSEMOTION:
                if e.buttons[0] and (pausado):
                    mouse_rel = pg.mouse.get_rel()
                    camera.pos.x -= mouse_rel[0]
                    camera.pos.y -= mouse_rel[1]
            
        tela.fill((0, 0, 0))
        tela.blit(fundo_img, (-camera.pos.x, -camera.pos.y))
        if not pausado and carro:
            carro.update(fundo_img)
            carro_meio = pg.Vector2(carro.roda1.x+30*math.cos(carro.angulo), carro.roda1.y+30*math.sin(carro.angulo))
            camera.seguir(carro_meio)

        if carro:
            carro.render(tela, camera)
        
        if carro and debug:
            tela.blit(fonte.render(str(carro.seguidor.rodar_seguidor(carro.sensores)), False, (255, 0, 0)), (5, 5))
        
        if pausado:
            tela.blit(pausado_img, (config.TELA_TAMANHO[0]//2-pausado_img.get_width()//2, 5))
            tela.blit(fonte.render(str(pg.mouse.get_rel()), 0, (255, 0, 0)), (5, 20))
        pg.display.update()
        clock.tick(config.FRAMERATE)

if __name__=="__main__":
    main()