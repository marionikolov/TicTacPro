"""
============================== TicTacPro ==============================
FILE: logic.py
MODIFIED: 08/12/2015
STATUS: Complete
FILE DESCRIPTION:
    The logic.py file is responsible for the game logic and behavour. It includes
    functions used to draw the board, validate and draw player moves, determine game
    outcome and quit the game.
USAGE:
    This file is not meant to be run independently. It serves as the codebase for the
    aforementioned functions and is used by nearly all other game files. Should the file
    be run on its own, it will prompt the user to run the TicTacProLauncher.py file.
"""

from main import *
from settings import *
    
def quitgame():
    """
    FUNCTION NAME: quitgame()
    PARAMETERS: 0
    FUNCTION DESCRIPTION:
        Excecutes the correct procedure for closing the program.
    """
    pygame.quit()
    sys.exit()
    
def gamewon(used):
    """
    FUNCTION NAME: gamewon()
    PARAMETERS: 1
                used (list; mandatory): the list representation of the board, containing either numbers 1-9, "x" or "o"
    FUNCTION DESCRIPTION:
        Decides whether the game is won taking in the used table which indicates the current game state
        and checking if there are three marks of the same kind in a row. The function return a tuple
        containing a boolean, corresponding to the state of the game, as its first value and an integer,
        corresponding to the win combination, as the second.
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
                pos (tuple; mandatory): a tuple containing the coordinate of the user mouse click (0-620, 0-690)
                used (list; mandatory): the list representation of the board, containing either numbers 1-9, "x" or "o"
    FUNCTION DESCRIPTION:
        Checks the mouse position coordinates against the board "hitboxes" and returns a boolean
        defining whether the click was in a valid location of a box.
    """
    rickcheck(pos) # Rickageddon check.
    
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
    """
    FUNCTION NAME: rickcheck()
    PARAMETERS: 1
                pos (tuple; mandatory): a tuple containing the coordinate of the user mouse click (0-620, 0-690)
    FUNCTION DESCRIPTION:
        Defines a super special move that rolls the screen!
    """
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
                turn (boolean; mandatory): a boolean value that determines whose turn it is; True for "x"; False for "o"
                pos (tuple; mandatory): a tuple containing the coordinate of a mouse click (0-620, 0-690)
                used (list; mandatory): the list representation of the board, containing either numbers 1-9, "x" or "o"
                images (list; mandatory): a list that stores the game's current image set for the board to use
    FUNCTION DESCRIPTION:
        Draws the game board and redraws it every time it is generated. It can handle different
        image sets using the images list passed in as a parameter.
    """
    if pos[0] in range(10,200) and pos[1] in range(10,200): # Top left box (7).
        if turn:
            screen.blit(images[1],(10,10))
            used[0]="x"
        else:
            screen.blit(images[2],(10,10))
            used[0]="o"
    elif pos[0] in range(210,400) and pos[1] in range(10,200): # Top center box (8).
        if turn:
            screen.blit(images[1],(210,10))
            used[1]="x"
        else:
            screen.blit(images[2],(210,10))
            used[1]="o"
    elif pos[0] in range(410,600) and pos[1] in range(10,200): # Top right box (9).
        if turn:
            screen.blit(images[1],(410,10))
            used[2]="x"
        else:
            screen.blit(images[2],(410,10))
            used[2]="o"    
    elif pos[0] in range(10,200) and pos[1] in range(210,400): # Middle left box (4).
        if turn:
            screen.blit(images[1],(10,210))
            used[3]="x"
        else:
            screen.blit(images[2],(10,210))
            used[3]="o"
    elif pos[0] in range(210,400) and pos[1] in range(210,400): # Middle center box (5).
        if turn:
            screen.blit(images[1],(210,210))
            used[4]="x"
        else:
            screen.blit(images[2],(210,210))
            used[4]="o"
    elif pos[0] in range(410,600) and pos[1] in range(210,400): # Middle right box (6).
        if turn:
            screen.blit(images[1],(410,210))
            used[5]="x"
        else:
            screen.blit(images[2],(410,210))
            used[5]="o"
    elif pos[0] in range(10,200) and pos[1] in range(410,600): # Bottom left box (1).
        if turn:
            screen.blit(images[1],(10,410))
            used[6]="x"
        else:
            screen.blit(images[2],(10,410))
            used[6]="o"
    elif pos[0] in range(210,400) and pos[1] in range(410,600): # Bottom center box (2).
        if turn:
            screen.blit(images[1],(210,410))
            used[7]="x"
        else:
            screen.blit(images[2],(210,410))
            used[7]="o"
    elif pos[0] in range(410,600) and pos[1] in range(410,600): # Bottom right box (3).
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
    FUNCTION NAME: drawline()
    PARAMETERS: 3
                wincombo (integer; mandatory): an integer that represents what combination has been achieved
                turn (boolean; mandatory): a boolean value that determines whose turn it is; True for "x"; False for "o"
                images (list; mandatory): a list that stores the game's current image set for the board to use
    FUNCTION DESCRIPTION:
        When the game is won, this function creates the effect of the flashing winning boxes.
    """
    xw=images[3]
    ow=images[4]
    x=images[1]
    o=images[2]
    for count in range(0,6):    # Creates the flashing effect according to the win pattern.
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
    print("Please launch the game from the TicTacProLauncher.py file.")
