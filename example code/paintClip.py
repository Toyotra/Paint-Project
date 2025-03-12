from pygame import *
from random import *
from math import *
    
screen = display.set_mode((800,600))
screen.fill((111,144,122))
pencilRect = Rect(20,80,40,40)
canvasRect = Rect(120,80,400,400)
draw.rect(screen, (255,255,255), canvasRect)
tool = "pencil"
running =True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False


    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    draw.rect(screen,(0,255,0),pencilRect,2)

    # If you forget to turn off your clipping, this will stop working
    if pencilRect.collidepoint(mx,my):
        draw.rect(screen,(255,0,0),pencilRect,2)
        if mb[0]==1:
            draw.rect(screen,(255,255,0),pencilRect,2)
            tool = "pencil"

    if mb[0]==1 and (canvasRect.collidepoint(mx,my) or canvasRect.collidepoint(omx,omy)):
        screen.set_clip(canvasRect)  # This says it only allows you to draw inside the canvas
        if tool == "pencil":
            draw.line(screen,(255,0,0),(omx,omy),(mx,my),5)

        screen.set_clip(None)   # Turn clipping off, so we can highlight tools

            
    omx, omy = mx,my
    display.flip()


quit()
