import pygame as pg
import config
from carro import Carro

pg.init()

def main():
    tela = pg.display.set_mode(config.TELA_TAMANHO)
    clock = pg.time.Clock()
    fonte = pg.font.SysFont("Calibri", 10)
    rodando = True

    carro = Carro(440, 920)
    roda_esquerda = roda_direita = False

    fundo_img = pg.image.load("imgs/fundo_teste.png").convert()

    while rodando:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                rodando = False
                return
            
            elif e.type==pg.KEYDOWN:
                if e.key==pg.K_a:
                    roda_esquerda = True

                elif e.key==pg.K_d:
                    roda_direita = True
            elif e.type==pg.KEYUP:
                if e.key==pg.K_a:
                    roda_esquerda = False

                elif e.key==pg.K_d:
                    roda_direita = False

        tela.blit(fundo_img, (0, 0))
        carro.update(roda_esquerda, roda_direita, tela)
        

        carro.render(tela)
        pg.display.update()
        clock.tick(config.FRAMERATE)

if __name__=="__main__":
    main()