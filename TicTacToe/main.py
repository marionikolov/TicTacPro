#installing all the modules required for this game
try:
    module="Time"
    import time
    module="Sys"
    import sys
    module="Pygame"
    import pygame
    module="Math"
    import math
    module="os"
    import os
#if none of these work then it will throw an error and tell you what you need
except:
    print("Error - You don't have the required modules installed!")
    print("Please install Module '{0}'! ".format(module))
    for count in range(0,50000000):
        pass
    raise SystemExit

pygame.init()
#game wide initalistion, starts all the relevant aspects to the game and loads the standard images
pygame.display.set_icon(pygame.image.load("images/misc/icon.png"))
screen=pygame.display.set_mode((610, 650))
clock = pygame.time.Clock()
images=[
pygame.image.load("images/classic/board.png"),
pygame.image.load('images/classic/x.png'),
pygame.image.load('images/classic/o.png'),
pygame.image.load("images/classic/xwon.png"),
pygame.image.load("images/classic/owin.png")
]
rick=pygame.image.load("images/misc/rick.png")
pygame.display.set_caption("TicTacPro Game","TicTacPro")

#all sound files from sounddogs.com royalty free and some editied by me
pygame.mixer.music.load("music/harder.mp3")
clicksound=pygame.mixer.Sound("music/fx/click.wav")
winsound=pygame.mixer.Sound("music/fx/win.wav")
losersound=pygame.mixer.Sound("music/fx/loser.wav")
nosound=pygame.mixer.Sound("music/fx/no.wav")
random=pygame.mixer.Sound("music/fx/random.wav")
mainmenuimg=pygame.image.load("images/menu/mainmenu.png")

#imports each file so the functions can be called and run in this program
try:
    from offline2p import *
    from offline1p import *
    from online import *
    from achievements import *
    from settings import *
    from firstgo import *
    from settings import *
    from logic import *
    from achievementsview import *
#if any files are missing will let you know what is missing
except ImportError:
    print("Error - You're missing game files!")
    print("Please download zip file again!")
    for count in range(0,50000000):
        pass
    raise SystemExit

def mainmenu(images, host="localhost", port=12341):
    """Runs the main menu, it opens the main menu, and allows you to access the rest of the game from here"""
    q = False
    while not q:
        screen=pygame.display.set_mode((610, 650))
        screen.blit(mainmenuimg,(0,0))
        pygame.draw.rect(screen, (0,0,0), [610, 0, 300, 700], 0)
        pygame.display.flip()
        ev = pygame.event.get()
        #if an event happens such as a keypress or mouse click it will run through this code
        for event in ev:
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(screen, (0,0,0), (10,610,600,40), 0)
                #checks whether the mouse click was on a button, which i have defined by coordinates 
                if pos[0] in range(50,560) and pos[1] in range(90,180):
                    print("Under Construction!")
                    #onlineconnect() #enter host and port information to connect to; then call the whosturn function and the online function
                    #whosturn=chooseturn()
                    online(True, images, host, port)
                    
                elif pos[0] in range(50,560) and pos[1] in range(190,285):
                    #runs the code that asks who goes first
                    whosturn=askquestion()
                    #launches the offline 1p state
                    offline1p("easy",whosturn,images)
                    
                elif pos[0] in range(50,560) and pos[1] in range(290,385):
                    whosturn=askquestion()
                    offline2p(whosturn,images)
                    
                elif pos[0] in range(50,560) and pos[1] in range(390,485):
                    possimages=settingmenu()
                    #if the stlye is changed then this code will run, changing what images the program uses
                    if possimages!=None:
                        images=possimages
                    
                elif pos[0] in range(50,560) and pos[1] in range(490,585):
                    achievementsview()

                elif pos[0] in range(534,600) and pos[1] in range(15,73):
                    #quits the game and leaves the loop
                    quitgame()
                    q=True
                

if __name__=="__main__":
    #this generates the splash screen for the program, this is run after the loading code as splash screens are traditionally used for that purpose and that's what we're replicating 
    pygame.display.set_icon(pygame.image.load("images/misc/icon.png"))
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    sega=pygame.mixer.Sound("music/fx/sega.wav")
    sega.play()
    screen = pygame.display.set_mode((200,200),pygame.NOFRAME)
    pygame.Surface([640,480], pygame.SRCALPHA, 32)
    splash=pygame.image.load("images\misc\splash.png")
    screen.blit(splash,(-30,-200))
    pygame.display.flip()
    time.sleep(2)
    pygame.display.set_icon(pygame.image.load("images/misc/icon.png"))
    screen=pygame.display.set_mode((610, 650))
    if len(sys.argv) > 1: # If the game was started through the launcher, pass the host and port from the arguments variable.
        mainmenu(images, sys.argv[1], int(sys.argv[2]))
    else: # If the game was started by opening the main.py file, show the following message and exit the game.
        print("Start the game using the TicTacProLauncher.py file.")
        #debug
        #mainmenu(images, "localhost", 12341)
        time.sleep(5)