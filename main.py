import pygame as pg
import config
pg.init()

def main():
    tela = pg.display.set_mode(config.TELA_TAMANHO)
    clock = pg.time.Clock()
    rodando = True

    while rodando:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                rodando = False
                return
        
        tela.fill(config.COR_FUNDO)

        pg.display.update()
        clock.tick(config.FRAMERATE)

if __name__=="__main__":
    main()