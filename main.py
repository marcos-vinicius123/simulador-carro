import pygame as pg
import src.config as config
from src.carro import Carro

pg.init()

def main():
    tela = pg.display.set_mode(config.TELA_TAMANHO)
    clock = pg.time.Clock()
    fonte = pg.font.SysFont("Calibri", 16)
    rodando = True
    pausado = False
    debug = False
    carro = None

    fundo_img = pg.image.load("imgs/fundo_teste.png").convert()
    pausado_img = fonte.render("pausado", False, (255, 0, 0))

    while rodando:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                rodando = False
                return
        
            elif e.type==pg.KEYUP:
                if e.key==pg.K_SPACE:
                    pausado =  not pausado
                elif e.key==pg.K_1:
                    debug = not debug

            elif e.type==pg.MOUSEBUTTONUP:
                carro = Carro(*pg.mouse.get_pos())

        tela.blit(fundo_img, (0, 0))
        if not pausado and carro:
            carro.update(tela)
        
        if carro:
            carro.render(tela)
        
        if carro and debug:
            tela.blit(fonte.render(str(carro.seguidor.rodar_seguidor(carro.sensores)), False, (255, 0, 0)), (5, 5))
        
        if pausado:
            tela.blit(pausado_img, (config.TELA_TAMANHO[0]//2-pausado_img.get_width()//2, 5))
        pg.display.update()
        clock.tick(config.FRAMERATE)

if __name__=="__main__":
    main()