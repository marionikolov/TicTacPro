#init stuff
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
except:
    print("Error - You don't have the required modules installed!")
    print("Please install Module '{0}'! ".format(module))
    for count in range(0,50000000):
        pass
    raise SystemExit
pygame.init()
#game wide initalistion, if its specific to one mode then do it in that games function
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
#pygame.mixer.music.play(-1)
#shared code for game logic etc
try:
    from offline2p import *
    from offline1p import *
    from online import *
    from achievements import *
    from settings import *
    from firstgo import *
    from settings import *
    from logic import *
except ImportError:
    print("Error - You're missing game files!")
    print("Please download zip file again!")
    for count in range(0,50000000):
        pass
    raise SystemExit

def mainmenu(images):
    q=False
    while not q:
        screen.blit(mainmenuimg,(0,0))
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                pygame.draw.rect(screen, (0,0,0), (10,610,600,40), 0)
                if pos[0] in range(50,560) and pos[1] in range(90,180):
                    print("Under Construction!")
                    whosturn=chooseturn()
                    online(whosturn)
                    
                elif pos[0] in range(50,560) and pos[1] in range(190,285):
                    whosturn=chooseturn()
                    offline1p("easy",whosturn,images)
                    
                elif pos[0] in range(50,560) and pos[1] in range(290,385):
                    whosturn=chooseturn()
                    offline2p(whosturn,images)
                    
                elif pos[0] in range(50,560) and pos[1] in range(390,485):
                    possimages=settingmenu()
                    if possimages!=None:
                        images=possimages
                    
                elif pos[0] in range(50,560) and pos[1] in range(490,585):
                    print("Under Construction!")
                    achievements()

                elif pos[0] in range(534,600) and pos[1] in range(15,73):
                    quitgame()
                    q=True
                
#funtion for the game running in offline 2 player mode
if __name__=="__main__":
    pygame.init()
    pygame.display.set_icon(pygame.image.load("images/misc/icon.png"))
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    sega=pygame.mixer.Sound("music/fx/sega.wav")
    sega.play()
    screen = pygame.display.set_mode((200,200),pygame.NOFRAME)
    pygame.Surface([640,480], pygame.SRCALPHA, 32)
    splash=pygame.image.load("images\misc\splash.png")
    screen.blit(splash,(-50,-60))
    pygame.display.flip()
    time.sleep(2)
    pygame.display.set_icon(pygame.image.load("images/misc/icon.png"))
    screen=pygame.display.set_mode((610, 650))
    mainmenu(images)
    
