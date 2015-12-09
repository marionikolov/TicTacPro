"""
============================== TicTacPro ==============================
FILE: Settings.py
MODIFIED: 15/11/2015
STATUS: Complete
FILE DESCRIPTION:
the Settings.py file is the state in which the program is changing visual
and audio settings about the game, such as the style or the music or the
difficulty.
"""
from main import *
from logic import *
#0-board
#1-x
#2-o
#3-xwin
#4-owin

def print(text,x=35,y=620):
    """
    FUNCTION NAME: print()
    PARAMETERS: 3
                text (string; mandatory): the output text intended to be shown to the user
                x (integer; optional): the X coordinate of the top left corner of the text output
                y (integer; optional): the Y coordinate of the top left corner of the text output              
    FUNCTION DESCRIPTION:
        Allows drawing text anywhere on the screen via the coordinates of the top left
        corner of the text displayed. If no coordinates are passed in, it defaults to the bottom left of
        the screen, which is designated as the display bar section. Has to be defined here do
        to some unknown bug.
    """
    pygame.draw.rect(screen, (64,0,64), (0,610,650,50), 0)
    font = pygame.font.Font(None, 32)
    textg = font.render(str(text), 4, (255, 255, 255))
    screen.blit(textg, (x,y))
    pygame.display.flip()


def settingmenu():
    settingsmenu=pygame.image.load("images/menu/settings/settingsmenu.png")
    q=False
    print("UN")
    while not q:
        #display menu screen
        screen.blit(settingsmenu,(0,0))
        pygame.display.flip()
        ev = pygame.event.get()
        #EDP
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                
                #pos is the coords for the mouse click
                pos = pygame.mouse.get_pos()
                #chooses which menu opens
                if pos[0] in range(70,260) and pos[1] in range(180,320):
                    images=stylemenu()
                elif pos[0] in range(350,540) and pos[1] in range(185,320):
                    songmenu()
                elif pos[0] in range(70,260) and pos[1] in range (380,510):
                    difficulty=difficultymenu()
                elif pos[0] in range(23,204) and pos[1] in range(540,600):                    #if images has been defined it will return it if not it will
                    #return nothing and the game will continue to use whatever
                    #images are already loaded
                    try:
                        return (difficulty,images)
                    
                    except:
                        try:
                            return (difficulty,None)
                        
                        except:
                            try:
                                return (None,images)
                            except:
                                return (None,None)

def songmenu():
    songmenu=pygame.image.load("images/menu/settings/songmenu.png")
    screen.blit(songmenu,(0,0))
    pygame.display.flip()
    q=False
    while not q:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
            
                if pos[0] in range(70,260) and pos[1] in range(180,320):
                    print("Music Changed - Harder!")
                    pygame.mixer.music.load("music/harder.mp3")
                    
                elif pos[0] in range(350,540) and pos[1] in range(180,320):
                    print("Music Changed - Lucky!")
                    pygame.mixer.music.load("music/lucky.mp3")
                    
                elif pos[0] in range(70,260) and pos[1] in range (380,510):
                    print("Music Changed - Nostalgia!")
                    pygame.mixer.music.load("music/oldschool.mp3")
                    
                elif pos[0] in range(350,540) and pos[1] in range(380,510):
                    print("Music Changed - Oh, Christmas Tree!")
                    pygame.mixer.music.load("music/christmas.mp3")
                    
                elif pos[0] in range(23,204) and pos[1] in range(540,600): # Back button.
                    q=True
                    
def difficultymenu():
    difficultymenuimg=pygame.image.load("images/menu/settings/difficultymenu.png")
    screen.blit(difficultymenuimg,(0,0))
    pygame.display.flip()
    q=False
    while not q:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
            #top left button
                if pos[0] in range(75,260) and pos[1] in range(190,320):
                    print("Difficulty set - Easy")
                    difficulty="easy"
             
                elif pos[0] in range(350,540) and pos[1] in range(185,320):
                    print("Difficulty set - Medium")
                    difficulty="medium"
                    
                elif pos[0] in range(75,260) and pos[1] in range(370,510):
                    print("Difficulty set - Hard")
                    difficulty="hard"
                    
                elif pos[0] in range(50,140) and pos[1] in range(560,590):
                    pass
                    try:
                        return difficulty
                    except:
                        return None
                elif event.type == pygame.QUIT:
                    quitgame()
                    
def stylemenu():
    stylesmenu=pygame.image.load("images/menu/settings/stylemenu.png")
    screen.blit(stylesmenu,(0,0))
    pygame.display.flip()
    q=False
    while not q:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
            #top left button
                
                if pos[0] in range(30,200) and pos[1] in range(160,300):
                    print("Board Loaded - Classic Board")
                    #the game pulls images from the list, change the content
                    #of the list, the images used changes, for ease of use 
                    images=[
                    pygame.image.load("images/classic/board.png"),
                    pygame.image.load('images/classic/x.png'),
                    pygame.image.load('images/classic/o.png'),
                    pygame.image.load("images/classic/xwon.png"),
                    pygame.image.load("images/classic/owin.png")
                    ]
             
                elif pos[0] in range(380,510) and pos[1] in range(160,300):
                    print("Board Loaded - Test Board")
                    images=[
                    pygame.image.load("images/test/board.png"),
                    pygame.image.load('images/test/x.png'),
                    pygame.image.load('images/test/o.png'),
                    pygame.image.load("images/test/xwon.png"),
                    pygame.image.load("images/test/owin.png")
                    ]
                    
                elif pos[0] in range(30,200) and pos[1] in range(370,510):
                    print("Board Loaded - Christmas Board")
                    images=[
                    pygame.image.load("images/christmas/board.png"),
                    pygame.image.load('images/christmas/x.png'),
                    pygame.image.load('images/christmas/o.png'),
                    pygame.image.load("images/christmas/xwon.png"),
                    pygame.image.load("images/christmas/owin.png")
                    ]
                    
                elif pos[0] in range(350,510) and pos[1] in range(370,510):
                    print("Board Loaded - Mushroom Board")
                    images=[
                    pygame.image.load("images/mushroom/board.png"),
                    pygame.image.load('images/mushroom/x.png'),
                    pygame.image.load('images/mushroom/o.png'),
                    pygame.image.load("images/mushroom/xwon.png"),
                    pygame.image.load("images/mushroom/owin.png")
                    ]
                    
                elif pos[0] in range(23,204) and pos[1] in range(540,600):
                    try:
                        return images
                    except:
                        return None
                                   
if __name__=="__main__":
    settingmenu()
