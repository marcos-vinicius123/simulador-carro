import pygame as pg
import math, sys
import src.config as config
from src.evolutivo import Evolutivo
from src.camera import Camera

pg.init()
sys.dont_write_bytecode = True

def main():
    tela = pg.display.set_mode(config.TELA_TAMANHO)
    clock = pg.time.Clock()
    fonte = pg.font.SysFont("Calibri", 16)
    rodando = True
    pausado = True
    debug = False
    carro_pos_inicial = None
    evolutivo = None
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
                if e.key==pg.K_SPACE:
                    pausado = not pausado
                
                if e.key==pg.K_r and evolutivo!=None:
                    evolutivo.gerar_geracao_inicial()
                    camera.seguir(evolutivo.carros[0].pos)

                elif e.key==pg.K_1:
                    debug = not debug

            elif e.type==pg.MOUSEBUTTONUP:
                if e.button==3 and carro_pos_inicial==None:
                    mouse_pos = pg.mouse.get_pos()
                    carro_pos_inicial = pg.Vector2(mouse_pos[0]+camera.pos.x, mouse_pos[1]+camera.pos.y)
                    evolutivo = Evolutivo(carro_pos_inicial)
                
                else:
                    pass
                    #adicionar checkpoint

            elif e.type==pg.MOUSEMOTION:
                mouse_rel = pg.mouse.get_rel() #se deixar dentro do if gera bugs
                if e.buttons[0]:
                    camera.pos.x -= mouse_rel[0]
                    camera.pos.y -= mouse_rel[1]
            
        tela.fill((0, 0, 0))
        tela.blit(fundo_img, (-camera.pos.x, -camera.pos.y))
        if not pausado and evolutivo:
            evolutivo.update(fundo_img)

        if evolutivo:
            evolutivo.render(tela, camera)
        
        if evolutivo and debug:
            pass
        
        if pausado:
            tela.blit(pausado_img, (config.TELA_TAMANHO[0]//2-pausado_img.get_width()//2, 5))
            tela.blit(fonte.render(str(pg.mouse.get_rel()), 0, (255, 0, 0)), (5, 20))
        pg.display.update()
        clock.tick(config.FRAMERATE)

if __name__=="__main__":
    main()