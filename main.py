#
#main.py
#Jad Menkara
#Death Note Themed MS Paint Project


from tkinter import *                
#from tkinter.colorchooser import *  # don't need this if you are not using colorchooser
from pygame import *
from tkinter import filedialog
import math as m
import sys #used for sys.exit()
import numpy as np #used for np.clip
import random #used for random in spray paint
init()
keys = key.get_pressed()

displayFont = font.Font("assets/evangelion-regular.otf", 30) #font used

thickness=1










# mixer.music.load("assets/music/Whats up people.mp3")
# mixer.music.play()
root = Tk()             # this initializes the Tk engine
root.withdraw()         # by default the Tk root will show a little window. This
                        # just hides that window
#setup
screen = display.set_mode((1400,900))
display.set_caption("Death Note Paint")
display.set_icon(image.load("assets/icon.png"))
running = True
background = image.load("assets/death-note-background.png") 
screen.blit(background, (0,0)) #displays background image
drawArea = Rect(170,150,1180,700) #canvas rect
mouseOnButton=False

currentColor = (0,0,0)

buttonList =[] #list of all button states
for i in range(30):
    buttonList.append(False)

class Button:
    def __init__(self, x, y, width, height, listVal, icon):
        
        #parameters for the button
        
        self.buttonRect =Rect(x,y,width,height)

        self.listVal=listVal
        self.colorA = [150,100,80]
        self.colorB = [50,50,50]
        self.currColor = [100,100,100]
        self.borderColor = [0,0,0]
        self.icon = icon
        self.opacityVal = 255
        self.buttonType=0
        
    def showButton(self, clicked, mouseX, mouseY):
        
        draw.rect(screen, (abs(self.currColor[0]), abs(self.currColor[1]),abs(self.currColor[2])), self.buttonRect)      
        draw.rect(screen, (self.borderColor[0], self.borderColor[1],self.borderColor[2]), self.buttonRect)    
        screen.blit(self.icon, (self.buttonRect.x+self.buttonRect.w/2-self.icon.get_width()/2, self.buttonRect.y+self.buttonRect.h/2-self.icon.get_height()/2))
        if self.buttonRect.collidepoint(mouseX,mouseY): #fade effect when hovering
            mouseOnButton=True
            self.currColor[0]-=0.2
            self.currColor[1]-=0.2
            self.currColor[2]-=0.2
            self.borderColor[0]+=0.2
            self.borderColor[1]+=0.2
            self.borderColor[2]+=0.2
            self.opacityVal-=0.5
            if self.buttonType==0:
                if clicked: #changes the value of list that is true when button is clicked, toggle
                    for i in range(len(buttonList)):
                        buttonList[i]=False
                    buttonList[self.listVal] = True
                
            elif self.buttonType==1:
                buttonList[self.listVal] = False
                if clicked: #changes the value of list that is true when button is clicked, not toggle, stays for only one frame
                    for i in range(len(buttonList)):
                        buttonList[i]=False
                    buttonList[self.listVal] = True
        else:
            self.currColor[0]+=0.4
            self.currColor[1]+=0.4
            self.currColor[2]+=0.4
            self.opacityVal+=0.4
            self.borderColor[0]-=0.2
            self.borderColor[1]-=0.2
            self.borderColor[2]-=0.2
        for i in range(3):
            self.currColor[i]=np.clip(self.currColor[i], self.colorB[i], self.colorA[i])
        for i in range(3):
            self.borderColor[i]=np.clip(self.currColor[i], 0,80)
        self.opacityVal = np.clip(self.opacityVal,150,255)
        self.icon.set_alpha(self.opacityVal)




class slider():
    def __init__(self,color1,color2,buttonWidth,buttonHeight,totalLength,totalHeight,x,y):
        
        #parameters for the slider
        
        self.color1=color1
        self.color2=color2
        
        self.buttonWidth=buttonWidth
        self.buttonHeight=buttonHeight
        
        self.totalLength=totalLength
        self.totalHeight=totalHeight
        self.xVal=x
        self.yVal=y
        
        self.currPercentage=0
        
        self.activated=False
        self.xShift=0
        
        
        self.imageInUse = False
        self.image=None
        
        

    
    def show(self,mouseX,mouseY,clicked,click):
        if self.imageInUse!=True:
            #draw.rect(screen,(0,0,0), Rect(self.xVal,self.yVal,self.totalLength,self.totalHeight),5)
            draw.rect(screen,self.color1, Rect(self.xVal,self.yVal,self.totalLength,self.totalHeight))
        else:
            screen.blit(self.image,(self.xVal,self.yVal))
            draw.rect(screen,(0,0,0), Rect(self.xVal,self.yVal,self.totalLength,self.totalHeight),5)
        
        if click:
            if Rect(self.xVal+self.currPercentage*(self.totalLength-self.buttonWidth)/100, self.yVal+self.totalHeight/2-self.buttonHeight/2,self.buttonWidth,self.buttonHeight).collidepoint(mouseX,mouseY):
                mouseOnButton=True
                self.activated=True
                self.xShift=mouseX-(self.xVal+self.currPercentage*(self.totalLength-self.buttonWidth)/100)

        if self.activated and clicked:
            self.currPercentage=np.clip(((mouseX-self.xVal-self.xShift)/(self.totalLength-self.buttonWidth)*100), 0, 100)
        else:
            self.activated=False
        
        
        draw.rect(screen,self.color2, Rect(self.xVal+self.currPercentage*(self.totalLength-self.buttonWidth)/100, self.yVal+self.totalHeight/2-self.buttonHeight/2,self.buttonWidth,self.buttonHeight))
        draw.rect(screen,(0,0,0), Rect(self.xVal+self.currPercentage*(self.totalLength-self.buttonWidth)/100, self.yVal+self.totalHeight/2-self.buttonHeight/2,self.buttonWidth,self.buttonHeight),5)
        
        return self.currPercentage
        
# colorSlider  = slider((255,255,255), (30,30,30), 60, 60, 256,60, 1100,20)
# colorSlider.imageInUse=True
# colorSlider.image=image.load("assets/color bar.png")
#print(colorSlider.image)



thicknessSlider = slider((255,255,255), (30,30,30), 60, 60, 256,60, 400,25) #thickness slider, object of slider class

#list of images used
imageList = [image.load("assets/paste-images/img1.png"),
             image.load("assets/paste-images/img2.png"),
             image.load("assets/paste-images/img3.png"),
             image.load("assets/paste-images/img4.png"),
             image.load("assets/paste-images/img5.png"),
             image.load("assets/paste-images/img6.png"),
             image.load("assets/paste-images/img7.png"),] #various images for paste function



buttonUp = False

class openFile(): #file open
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")]) #gets path of file
        if result:
            screen.set_clip(drawArea)#used to close all surfaces blited to screen to canvas   
            screen.blit(image.load(result), (drawArea)) #blits image to screen
            screen.set_clip(None)
openFileA  = openFile()

class saveFile(): #file save
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        result = filedialog.asksaveasfilename()  #gets path of file
        if result:
            image.save(screen.subsurface(drawArea).copy(), result) #saves image
saveFileA = saveFile()


#pencil tool
class pencil():
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if n:
            screen.set_clip(drawArea)
            draw.line(screen, currentColor, (oldMX,oldMY),(newMX,newMY),thickness)
            screen.set_clip(None)
            
class sprayPaint():
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if n:
            if drawArea.collidepoint(mx,my): #only runs if mouse hovers over canvas
                screen.set_clip(drawArea)
                for i in range(10):
                    draw.circle(screen, currentColor, (random.randint(mx-thickness*15,mx+thickness*15),random.randint(my-thickness*15,my+thickness*15)),thickness) #gets random point within square of mx,my, blits 10 circles to make illusion of spray paint
                time.wait(20)
                screen.set_clip(None)
sprayPaintA = sprayPaint()

class marker():
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if n:
            screen.set_clip(drawArea) 
            forVal= m.ceil(m.dist([mx,my],[oldMX, oldMY])/3)
            #print(forVal)
            for i in range(forVal):
                draw.circle(screen, currentColor,  (mx+(mx-oldMX)/forVal*i, my+(my-oldMY)/forVal*i),thickness*5)
            screen.set_clip(None)
            
markerA = marker()            
            

class eraser():
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if n:
            screen.set_clip(drawArea)
            #eraseRect = (newMX,newMY,60,60)
            draw.circle(screen, (255,255,255), (mx,my), thickness*6)
            screen.set_clip(None)
eraserA = eraser()

class line():
    def __init__(self):
        self.initiate=False
        self.startX, self.startY = 0, 0
        self.pasteSurface = None

    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        # print(self.initiate)
        if clickingVal:
            self.initiate=True
            self.startX= mx
            self.startY= my
            self.pasteSurface=screen.subsurface(drawArea).copy()
            # print("SUFFOCATE")
        if self.initiate:
            screen.set_clip(drawArea)
            screen.blit(self.pasteSurface, (drawArea))
            draw.line(screen, currentColor, (self.startX,self.startY), (mx,my),thickness)
            screen.set_clip(None)
        if buttonUp:
                self.initiate=False
                
                
class rectangle():
    def __init__(self):
        self.initiate=False
        self.startX, self.startY = 0, 0
        self.pasteSurface = None

    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if clickingVal:
            self.initiate=True
            self.startX= mx
            self.startY= my
            self.pasteSurface=screen.subsurface(drawArea).copy()
        if self.initiate:
            screen.set_clip(drawArea)
            screen.blit(self.pasteSurface, (drawArea))
            
            
            #I could've used Rect.normalise here, but i didnt have enough time to impliment
            if mx<self.startX:
                if my<self.startY:
                    draw.rect(screen, currentColor, (mx,my, self.startX-mx,self.startY-my))
                    draw.rect(screen, (0,0,0), (mx,my, self.startX-mx,self.startY-my),thickness)
                    #print(3)
                else:
                    draw.rect(screen, currentColor, (mx,self.startY, self.startX-mx,my-self.startY))
                    draw.rect(screen, (0,0,0), (mx,self.startY, self.startX-mx,my-self.startY),thickness)
                   # print(2)
            elif my<self.startY:
                draw.rect(screen, currentColor, (self.startX,my, mx-self.startX,self.startY-my))
                draw.rect(screen, (0,0,0), (self.startX,my, mx-self.startX,self.startY-my),thickness)
                #print(1)
            else:
                draw.rect(screen, currentColor, (self.startX,self.startY,mx-self.startX,my-self.startY))
                draw.rect(screen, (0,0,0), (self.startX,self.startY,mx-self.startX,my-self.startY),thickness)
                #print(0)
            screen.set_clip(None)
        if buttonUp:
                self.initiate=False
rectangleA = rectangle()



class circle(): #circle function
    def __init__(self):
        self.initiate=False
        self.startX, self.startY = 0, 0 #point of circle centre
        self.pasteSurface = None

    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if clickingVal:
            self.initiate=True
            self.startX= mx
            self.startY= my
            self.pasteSurface=screen.subsurface(drawArea).copy()
        if self.initiate:
            screen.set_clip(drawArea)
            screen.blit(self.pasteSurface, (drawArea))
            
            #draws 2 circles, on for fill, one for outline
            draw.ellipse(screen, currentColor,(min(self.startX,mx),min(self.startY,my),abs(mx-self.startX),abs(my-self.startY)))
            draw.ellipse(screen, (0,0,0),(min(self.startX,mx),min(self.startY,my),abs(mx-self.startX),abs(my-self.startY)),thickness)
            #print(0)
            screen.set_clip(None)
        if buttonUp:
                self.initiate=False
circleA = circle()

     
            
            
            
            
            
lineA = line()
                
                
    
#image paste tool
class imagePaste():
    def __init__(self, currImage):
        self.currImage=currImage
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,currClick):
        if clickingVal and drawArea.collidepoint(mx,my):
            screen.set_clip(drawArea)
            screen.blit(self.currImage,  (newMX-self.currImage.get_width()/2,newMY-self.currImage.get_height()/2))
            screen.blit(background, (0,0))
            screen.set_clip(None)



#undo, adds to redolist, removes from undo list
class undoFunc():
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if len(savedCanvasA)>1:
            
            
            popped = savedCanvasA.pop()
            savedCanvasB.append(popped)
            screen.blit(savedCanvasA[-1], (drawArea))
            
#redo, removes from redolist, adds to undo list
class redoFunc():
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if len(savedCanvasB)>0:
                       
            popped = savedCanvasB.pop()
            savedCanvasA.append(popped)
            screen.blit(savedCanvasA[-1], (drawArea))


#clears screen,draws white rect on canvas        
class clear():
    def __init__(self):
        pass
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        draw.rect(screen, (255,255,255), drawArea)
clearA = clear()            



#list of available keys you can press for txt function
keyList = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '`', '-', '=', '[', ']', ';', '\'', ',', '.', '/',
]


class deathNoteText():
    def __init__(self):
        #parameters for text
        self.typing =False
        self.currentText=""
        self.og = None
        self.textLocation = [0,0]
        self.textTimer = 0  
        self.states = ["","|"]
        self.currentState=0
    def run(self,newMX,newMY,oldMX,oldMY,clickingVal,n):
        if  clickingVal and drawArea.collidepoint(mx,my):
            self.typing =True
            self.og=screen.subsurface(drawArea).copy()
            self.textLocation = [mx,my]
        if self.typing:
            if currentKey == K_RETURN: # if key is return, reset the string
                for i in range(len(buttonList)):
                    buttonList[i]=False
                self.typing =False
                self.textTimer=0
            else:
                if currentKey!=None:
                    if currentKey == K_BACKSPACE:
                        self.currentText = self.currentText[:-1]
                    if currentKey == K_SPACE:
                        self.currentText +=" "
                    else:
                        if key.name(currentKey) in keyList:
                            self.currentText += key.name(currentKey)
                            
                            
            self.textTimer +=1 # used for the "|" time function
            self.textTimer = self.textTimer%240
            self.currentState = self.textTimer//120 

            screen.blit(self.og, drawArea) #displays text to screen
            screen.blit(displayFont.render(self.states[self.currentState],True,currentColor), (self.textLocation[0],self.textLocation[1]))           
            screen.blit(displayFont.render(self.currentText, True, currentColor), (self.textLocation[0]+10,self.textLocation[1]))
        else:
            self.currentText=""  
deathNoteTextA =deathNoteText()
            
        
        
            
        
            

undoA = undoFunc()
redoA =  redoFunc()


pencilA=pencil()
image1 = imagePaste(imageList[0]) #images for image paste tool
image2 = imagePaste(imageList[1])
image3 = imagePaste(imageList[2])
image4 = imagePaste(imageList[3])
image5 = imagePaste(imageList[4])
image6 = imagePaste(imageList[5])
image7 = imagePaste(imageList[6])
       

    
       
#assigns functions to a dictionary, this is slightly easier to do than an array because we know the key as the function, rather than the index       
functions = {0:saveFileA,
             1:openFileA,
             2:pencilA,
             3:eraserA,
             4:markerA,
             5:lineA,
             6:rectangleA,
             7:circleA,
             8:pencilA,
             9:image1,
             10:image2,
             11:image3,
             12:image4,
             13:image5,
             14:image6,
             15:image7,
             16:redoA,
             17:undoA,
             18:sprayPaintA ,
             19:deathNoteTextA,
             20:clearA,
             21:pencilA,
             22:pencilA,

             }      
       
       
       
# creates buttons as objects of the Button class
saveButton = Button(80,20,50,50,0,image.load("assets/save.png"))
loadButton = Button(20,20,50,50,1,image.load("assets/open-folder.png"))
saveButton.buttonType=1
loadButton.buttonType=1


pencilButton = Button(20,80,50,50,2,image.load("assets/pencil.png"))
eraserButton = Button(80,80,50,50,3,image.load("assets/eraser.png"))
markerButton = Button(20,140,50,50,4,image.load("assets/marker.png"))

diagonolButton = Button(177,20,50,50,5,image.load("assets/diagonal-line.png"))
rectangleButton = Button(237,20,50,50,6,image.load("assets/rectangle.png"))
ovalButton = Button(297,20,50,50,7,image.load("assets/oval.png"))
deathNoteButton = Button(177,80,50,50,19,image.load("assets/t.png"))
sprayPaintButton = Button(237,80,50,50,18,image.load("assets/spray-paint.png"))
clearButton = Button(297,80,50,50,20,image.load("assets/bin.png"))
clearButton.buttonType=1


redoButton = Button(80,210,50,50,16,image.load("assets/forward.png"))
undoButton = Button(20,210,50,50,17,image.load("assets/undo.png"))
redoButton.buttonType=1
undoButton.buttonType=1




#pasteImages
image1Button = Button(20,320,80,80,9,transform.scale_by(image.load("assets/paste-images/img1.png"), 1/3))
image2Button = Button(20,410,80,80,10,transform.scale_by(image.load("assets/paste-images/img2.png"), 1/4))
image3Button = Button(20,500,80,80,11,transform.scale_by(image.load("assets/paste-images/img3.png"), 1/3))
image5Button = Button(20,590,80,80,13,transform.scale_by(image.load("assets/paste-images/img5.png"), 1/3))



image6Button = Button(20,680,80,80,14,transform.scale_by(image.load("assets/paste-images/img6.png"), 1/3))
image7Button = Button(20,770,80,80,15,transform.scale_by(image.load("assets/paste-images/img7.png"), 1/3))





draw.rect(screen, (255,255,255), drawArea)
currPasteImage=0



colorChart=image.load("assets/spectrumChart.jpg")
colorChartRect = colorChart.get_rect()
colorChartRect.x=1200
colorChartRect.y=20



savedCanvasA= [] #undo list
savedCanvasB= [] #redo list
savedCanvasA.append(screen.subsurface(drawArea).copy()) #adds current screen to undo list

textDisplayA = displayFont.render("Color:", True, currentColor)
textDisplay = displayFont.render("(0, 0, 0, 0)", True, currentColor)
textDisplayThickness = displayFont.render("Thickness: 1", True, (255,255,255))


#running Loop
oldMouseX,oldMouseY = mouse.get_pos()
while running:
    
    currentKey = None
    
    clickValue= False
    buttonUp = False    
    
    #checks for events
    for e in event.get():
        if e.type == QUIT:
            running = False
            quit()
            sys.exit()           
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                clickValue = True              
        if e.type == MOUSEBUTTONUP:
            if e.button == 1:
                buttonUp = True
                currCanvas =screen.subsurface(drawArea).copy() #if mousebuttonup is clicked, and the the canvas has changed, an item is added to our uno list
                if (surfarray.pixels3d(savedCanvasA[-1]) == surfarray.pixels3d(currCanvas)).all()==False:
                    savedCanvasA.append(screen.subsurface(drawArea).copy())
                    savedCanvasB=[]
        if e.type == KEYDOWN:
            currentKey =  e.key

                    

    #mouse input
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    
    draw.rect(screen, (100,100,100), (390, 15,  280, 115))
    
    thickness=int(np.clip(thicknessSlider.show(mx,my,mb[0],clickValue)//10,1,10)) #changes thickness via slider
    textDisplayThickness = displayFont.render(f"Thickness: {int(thickness)}", True, (255,255,255))
    screen.blit(textDisplayThickness, (400, 90))
    
    #print(currentColor)
    #displays buttons to screen
    saveButton.showButton(clickValue, mx,my)
    loadButton.showButton(clickValue, mx,my)
    pencilButton.showButton(clickValue, mx,my)
    eraserButton.showButton(clickValue, mx,my)
    markerButton.showButton(clickValue, mx,my)
    
    diagonolButton.showButton(clickValue, mx,my)
    rectangleButton.showButton(clickValue, mx,my)
    ovalButton.showButton(clickValue, mx,my)
    deathNoteButton.showButton(clickValue, mx,my)
    sprayPaintButton.showButton(clickValue, mx,my)
    
    image1Button.showButton(clickValue, mx,my)
    image2Button.showButton(clickValue, mx,my)
    image3Button.showButton(clickValue, mx,my)
    image5Button.showButton(clickValue, mx,my)
    image6Button.showButton(clickValue, mx,my)
    image7Button.showButton(clickValue, mx,my)
    
    redoButton.showButton(clickValue,mx,my)
    undoButton.showButton(clickValue,mx,my)
    clearButton.showButton(clickValue,mx,my)
    
    
    #colorSlider.show(mx,my,mb[0],click)
    draw.rect(screen,  (150,150,150), (1000,10,350,125)) #displays color chart 
    draw.rect(screen,  (255,255,255), (1000,10,350,125),2) 
    screen.blit(colorChart, (1200,20))
    screen.blit(textDisplayA, (1010,20))
    screen.blit(textDisplay, (1010,50))
    
    if colorChartRect.collidepoint(mx,my): #checks if mouse is on color wheel
        draw.rect(screen,(255,255,255),colorChartRect,4)
        if mb[0]:
            currentColor = screen.get_at((mx,my))
            textDisplay = displayFont.render(f"{currentColor}", True, currentColor)
    else:
        draw.rect(screen,(0,0,0),colorChartRect,4)
    
    
    
    
    
    #runs functions from buttons
    for i in range(len(buttonList)):
        if buttonList[i]:
            if i!=19:
                deathNoteTextA.currentText=""
            functions[i].run(mx,my,oldMouseX,oldMouseY,clickValue,mb[0])
    
    
    
    
    
    mouseOnButton=False
    #old mx/my
    oldMouseX = mx
    oldMouseY = my
    #updates screen  
    display.flip()
    #print(len(savedCanvasA),len(savedCanvasB))
    
    
    
quit()
