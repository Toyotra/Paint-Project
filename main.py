import pygame as pg
import math
import sys
screen = pg.display.set_mode((1500,800))
screen.fill((50,50,50))
while True:
    for event in pg.event.get():
        if event.type=pg.quit():
            pg.quit()
            sys.exit()

    
    pg.display.flip()
