'''
tkinter is a Graphical User Interface toolkit.
tk == toolkit
inter == interface to your python program

Unlike pygame, you don't need to install anything new to use tkinter. You can
do a lot with tkinter. I suggest that you only use it for dialog boxes. The ones
below are some of the most useful dialogs, but certainly not the only ones.
'''
from tkinter import *                
from tkinter.colorchooser import *  # don't need this if you are not using colorchooser
from pygame import *
from tkinter import filedialog

root = Tk()             # this initializes the Tk engine
root.withdraw()         # by default the Tk root will show a little window. This
                        # just hides that window

screen = display.set_mode((800,600))
screen.fill((0,128,192))
openRect = Rect(20,80,40,40)
saveRect = Rect(65,80,40,40)
colourRect = Rect(110,80,40,40)

running =True
draw.rect(screen,(0,255,0),openRect,2)
draw.rect(screen,(0,255,0),saveRect,2)
drawcolor = (0,0,0)

while running:
    click = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                click = True

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()

    if click:
        if openRect.collidepoint(mx,my):
            result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")]) # There are some options you can use to make these look nicer.
            print(result)
        elif saveRect.collidepoint(mx,my):
            result = filedialog.asksaveasfilename() ###
            print(result)

    display.flip()


quit()
