import pygame as pg
import math
import sys


screen = pg.display.set_mode((1500,800))
screen.fill((50,50,50))

running =  True
while running:
    for event in pg.event.get():
        if event.type==pg.quit():
            running=False
            pg.quit()
            sys.exit()

    
    pg.display.flip()
