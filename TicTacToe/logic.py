"""
============================== TicTacPro ==============================
FILE: Logic.py
MODIFIED: 15/11/2015
STATUS: Complete
FILE DESCRIPTION:
The logic.py file has code used by multiple files of the program, a shared code file
such as the game logic, drawing the board, print functions etc
USAGE:
This is a client file as it is for the drawing and logic aspect of the game.
"""

from main import *
from settings import *

def print(text,x=40,y=615):
    """
    FUNCTION NAME: printcoord()
    PARAMETERS: 3
        text (string; mandatory): 
        x (integer; optional"): The X co-ordinate of the top left corner of the text output
        y (integer; optional"): The Y co-ordinate of the top left corner of the text output
                
    FUNCTION DESCRIPTION:
    lets you draw text anywhere on the screen via the coordinates of the top left
    corner of the text displayed, if no coordinates are passed in it defaults to the bottom left of
    the screen which I have designated as the display bar section.
    """
    pygame.draw.rect(screen, (0,0,0), (10,610,600,40), 0)
    font = pygame.font.Font(None, 32)
    textg = font.render(str(text), 4, (255, 255, 255))
    screen.blit(textg, (x,y))
    pygame.display.flip()
    
def quitgame():
    """
    FUNCTION NAME: quitgame()
    PARAMETERS: 0
    FUNCTION DESCRIPTION:
        excecutes the correct procedure for closing the program.
    """
    pygame.quit()
    sys.exit()
    
def gamewon(used):
    """
    FUNCTION NAME: gamewon()
    PARAMETERS: 1
        used (list; mandatory): The list representation of the board, either 1-9, "x" or "o".

    FUNCTION DESCRIPTION:
        Decides wether the game is won taking in the used table
        that indicates current game state and checking if there are 3 in a row
        """
    if used[0]==used[1] and used[1]==used[2]: return (True,1)
    elif used[3]==used[4] and used[4]==used[5]: return (True,2)
    elif used[6]==used[7] and used[7]==used[8]: return (True,3)
    elif used[0]==used[3] and used[3]==used[6]: return (True,4)
    elif used[1]==used[4] and used[4]==used[7]: return (True,5)
    elif used[2]==used[5] and used[5]==used[8]: return (True,6)
    elif used[0]==used[4] and used[4]==used[8]: return (True,7)
    elif used[2]==used[4] and used[4]==used[6]: return (True,8)
    else: return (False,999)
    
def validmove(pos,used):
    """
    FUNCTION NAME: validmove()
    PARAMETERS: 2
        pos (tuple; mandatory): A tuple containing the coordinate of a mouse click (0-620,0-690)
        used (list; mandatory): The list representation of the board, either 1-9, "x" or "o".

    FUNCTION DESCRIPTION:
        Checks the mouse position coordinates against the board "hitboxes" and returns a boolean
        defining wether the click was in a valid location of a box.
    """
    #rickageddon
    rickcheck(pos)
    
    if pos[0] in range(10,200) and pos[1] in range(10,200): sqr=0       
    elif pos[0] in range(210,400) and pos[1] in range(10,200): sqr=1
    elif pos[0] in range(410,600) and pos[1] in range(10,200): sqr=2
    elif pos[0] in range(10,200) and pos[1] in range(210,400): sqr=3      
    elif pos[0] in range(210,400) and pos[1] in range(210,400): sqr=4
    elif pos[0] in range(410,600) and pos[1] in range(210,400): sqr=5
    elif pos[0] in range(10,200) and pos[1] in range(410,600): sqr=6     
    elif pos[0] in range(210,400) and pos[1] in range(410,600): sqr=7
    elif pos[0] in range(410,600) and pos[1] in range(410,600): sqr=8
    else:
        return False
    
    if used[sqr] not in ["o","x"]:
            return True
    else:
        return False

def rickcheck(pos):
    """super special move that rolls the screen"""
    if pos[0] in range(580,610) and pos[1] in range(610,640):
        cena=pygame.image.load("images/misc/cena.png")
        pygame.image.save(screen,"images/misc/temp.png")
        pygame.mixer.music.load("music/special.mp3")
        pygame.mixer.music.play(-1)
        posit=(-200)
        num=10
        while num<40:
            if posit>500:
                posit=(-200)
            screen.blit(rick,(posit,-50))
            screen.blit(rick,(posit+num,50))
            screen.blit(rick,(posit+num*2,150))
            screen.blit(rick,(posit+num*3,250))
            screen.blit(rick,(posit+num*4,350))
            if num>15:
                screen.blit(rick,(posit,-50))
                screen.blit(rick,(50,posit+num))
                screen.blit(rick,(150,posit+num*2))
                screen.blit(rick,(250,posit+num*3))
                screen.blit(rick,(350,posit+num*4))
            pygame.display.flip()
            num+=0.5
            posit+=20
            time.sleep(0.2)
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    screen.blit(rick,(pos[0]-50,pos[1]-50))
                    pygame.display.flip()
        pygame.mixer.music.pause()
        random.play()
        time.sleep(1.6)
        screen.blit(cena,(-350,-50))
        pygame.display.flip()
        time.sleep(4.4)
        pygame.mixer.music.unpause()
        
        temp=pygame.image.load("images/misc/temp.png")
        screen.blit(pygame.image.load("images/misc/temp.png"),(0,0))
        pygame.display.flip()
        
def drawbox(turn,pos,used,images):
    """
    FUNCTION NAME: drawbox()
    PARAMETERS: 4
        turn (boolean; mandatory): A boolean value that determines who's turn it is, True for x. False for o)
        pos (tuple; mandatory): A tuple containing the coordinate of a mouse click (0-620,0-690)
        used (list; mandatory): The list representation of the board, either 1-9, "x" or "o".
        images (list; mandatory): A list that stores the games current images for the board to use
         and it stored as objects in a list

    FUNCTION DESCRIPTION:
        Draws the game board, redraws it every time the board is generated. can handle different
        images sets thanks to the image list
    """
    #box7
    if pos[0] in range(10,200) and pos[1] in range(10,200): # and used :
        if turn:
            screen.blit(images[1],(10,10))
            used[0]="x"
        else:
            screen.blit(images[2],(10,10))
            used[0]="o"
    #box8        
    elif pos[0] in range(210,400) and pos[1] in range(10,200):
        if turn:
            screen.blit(images[1],(210,10))
            used[1]="x"
        else:
            screen.blit(images[2],(210,10))
            used[1]="o"
    #box9
    elif pos[0] in range(410,600) and pos[1] in range(10,200):
        if turn:
            screen.blit(images[1],(410,10))
            used[2]="x"
        else:
            screen.blit(images[2],(410,10))
            used[2]="o"    
    #box4
    elif pos[0] in range(10,200) and pos[1] in range(210,400):
        if turn:
            screen.blit(images[1],(10,210))
            used[3]="x"
        else:
            screen.blit(images[2],(10,210))
            used[3]="o"
    #box5        
    elif pos[0] in range(210,400) and pos[1] in range(210,400):
        if turn:
            screen.blit(images[1],(210,210))
            used[4]="x"
        else:
            screen.blit(images[2],(210,210))
            used[4]="o"
    #box6
    elif pos[0] in range(410,600) and pos[1] in range(210,400):
        if turn:
            screen.blit(images[1],(410,210))
            used[5]="x"
        else:
            screen.blit(images[2],(410,210))
            used[5]="o"
    #box1
    elif pos[0] in range(10,200) and pos[1] in range(410,600):
        if turn:
            screen.blit(images[1],(10,410))
            used[6]="x"
        else:
            screen.blit(images[2],(10,410))
            used[6]="o"
    #box2        
    elif pos[0] in range(210,400) and pos[1] in range(410,600):
        if turn:
            screen.blit(images[1],(210,410))
            used[7]="x"
        else:
            screen.blit(images[2],(210,410))
            used[7]="o"
    #box3
    elif pos[0] in range(410,600) and pos[1] in range(410,600):
        if turn:
            screen.blit(images[1],(410,410))
            used[8]="x"
        else:
            screen.blit(images[2],(410,410))
            used[8]="o"
            
    turn=not turn
    pygame.display.flip()
    return used

def drawline(wincombo,turn,images):
    """ 
    FUNCTION NAME: drawbox()
    PARAMETERS: 3
        wincombo (integer; mandatory): An integer that represents what combination has been achieved
        turn (boolean; mandatory): A boolean value that determines who's turn it is, True for x. False for o)
        images (list; mandatory): A list that stores the games current images for the board to use,
        stored as objects in a list

    FUNCTION DESCRIPTION:
        When the game is won it creates the effect of the flashing winning boxes
    """
    xw=images[3]
    ow=images[4]
    x=images[1]
    o=images[2]
    #creates the flashing effect
    for count in range(0,6):
        #changes every other time
        if count/2==count//2:
            winsound.play()
            if wincombo==1:
                if turn:screen.blit(xw,(10,10)),screen.blit(xw,(210,10)),screen.blit(xw,(410,10))
                else:screen.blit(ow,(10,10)),screen.blit(ow,(210,10)),screen.blit(ow,(410,10))
                    
            elif wincombo==2:
                if turn:screen.blit(xw,(10,210)),screen.blit(xw,(210,210)),screen.blit(xw,(410,210))
                else:screen.blit(ow,(10,210)),screen.blit(ow,(210,210)),screen.blit(ow,(410,210))
               
            elif wincombo==3:
                if turn:screen.blit(xw,(10,410)),screen.blit(xw,(210,410)),screen.blit(xw,(410,410))
                else:screen.blit(ow,(10,410)),screen.blit(ow,(210,410)),screen.blit(ow,(410,410))
                    
            elif wincombo==4:
                if turn:screen.blit(xw,(10,10)),screen.blit(xw,(10,210)),screen.blit(xw,(10,410))
                else:screen.blit(ow,(10,10)),screen.blit(ow,(10,210)),screen.blit(ow,(10,410))
                    
            elif wincombo==5:
                if turn:screen.blit(xw,(210,10)),screen.blit(xw,(210,210)),screen.blit(xw,(210,410))
                else:screen.blit(ow,(210,10)),screen.blit(ow,(210,210)),screen.blit(ow,(210,410))
                    
            elif wincombo==6:
                if turn:screen.blit(xw,(410,10)),screen.blit(xw,(410,210)),screen.blit(xw,(410,410))
                else:screen.blit(ow,(410,10)),screen.blit(ow,(410,210)),screen.blit(ow,(410,410))
                    
            elif wincombo==7:
                if turn:screen.blit(xw,(10,10)),screen.blit(xw,(210,210)),screen.blit(xw,(410,410))
                else:screen.blit(ow,(10,10)),screen.blit(ow,(210,210)),screen.blit(ow,(410,410))
                    
            elif wincombo==8:
                if turn:screen.blit(xw,(410,10)),screen.blit(xw,(210,210)),screen.blit(xw,(10,410))
                else:screen.blit(ow,(410,10)),screen.blit(ow,(210,210)),screen.blit(ow,(10,410))
        else:
            if wincombo==1:
                if turn:screen.blit(x,(10,10)),screen.blit(x,(210,10)),screen.blit(x,(410,10))
                else:screen.blit(o,(10,10)),screen.blit(o,(210,10)),screen.blit(o,(410,10))
                    
            elif wincombo==2:
                if turn:screen.blit(x,(10,210)),screen.blit(x,(210,210)),screen.blit(x,(410,210))
                else:screen.blit(o,(10,210)),screen.blit(o,(210,210)),screen.blit(o,(410,210))
               
            elif wincombo==3:
                if turn:screen.blit(x,(10,410)),screen.blit(x,(210,410)),screen.blit(x,(410,410))
                else:screen.blit(o,(10,410)),screen.blit(o,(210,410)),screen.blit(o,(410,410))
                    
            elif wincombo==4:
                if turn:screen.blit(x,(10,10)),screen.blit(x,(10,210)),screen.blit(x,(10,410))
                else:screen.blit(o,(10,10)),screen.blit(o,(10,210)),screen.blit(o,(10,410))
                    
            elif wincombo==5:
                if turn:screen.blit(x,(210,10)),screen.blit(x,(210,210)),screen.blit(x,(210,410))
                else:screen.blit(o,(210,10)),screen.blit(o,(210,210)),screen.blit(o,(210,410))
                    
            elif wincombo==6:
                if turn:screen.blit(x,(410,10)),screen.blit(x,(410,210)),screen.blit(x,(410,410))
                else:screen.blit(o,(410,10)),screen.blit(o,(410,210)),screen.blit(o,(410,410))
                    
            elif wincombo==7:
                if turn:screen.blit(x,(10,10)),screen.blit(x,(210,210)),screen.blit(x,(410,410))
                else:screen.blit(o,(10,10)),screen.blit(o,(210,210)),screen.blit(o,(410,410))
                    
            elif wincombo==8:
                if turn:screen.blit(x,(410,10)),screen.blit(x,(210,210)),screen.blit(x,(10,410))
                else:screen.blit(o,(410,10)),screen.blit(o,(210,210)),screen.blit(o,(10,410))
        pygame.display.flip()
        time.sleep(0.5)

if __name__=="__main__":
    print("you need to run the main program")
