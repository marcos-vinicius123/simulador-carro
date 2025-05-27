import pygame as pg
import config
from carro import Carro

pg.init()

def main():
    tela = pg.display.set_mode(config.TELA_TAMANHO)
    clock = pg.time.Clock()
    rodando = True

    carro = Carro(config.TELA_TAMANHO[0]//2, config.TELA_TAMANHO[1]//2)
    roda_esquerda = roda_direita = False

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
                
        carro.update(roda_esquerda, roda_direita)
        tela.fill(config.COR_FUNDO)

        carro.render(tela)

        pg.display.update()
        clock.tick(config.FRAMERATE)

if __name__=="__main__":
    main()