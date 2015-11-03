#init stuff
import pygame, math, sys, time, os
from os.path import dirname, realpath, abspath
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
special=pygame.mixer.Sound("music/special.wav")
pygame.mixer.music.load("music/music.wav")
clicksound=pygame.mixer.Sound("music/click.wav")
winsound=pygame.mixer.Sound("music/win.wav")
losersound=pygame.mixer.Sound("music/loser.wav")
nosound=pygame.mixer.Sound("music/no.wav")
mainmenuimg=pygame.image.load("images/menu/mainmenu.png")
#shared code for game logic etc
from offline2p import *
from offline1p import *
from online import *
from achievements import *
from settings import *
from firstgo import *
from settings import *
from logic import *

def mainmenu(images):
    q=False
    while not q:
        screen.blit(mainmenuimg,(0,0))
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(50,560) and pos[1] in range(90,180):
                    whosturn=chooseturn()
                    online(whosturn)
                    
                elif pos[0] in range(50,560) and pos[1] in range(190,285):
                    whosturn=chooseturn()
                    offline1p("easy",whosturn,images)
                    
                elif pos[0] in range(50,560) and pos[1] in range(290,385):
                    whosturn=chooseturn()
                    offline2p(whosturn,images)
                    
                elif pos[0] in range(50,560) and pos[1] in range(390,485):
                    images=settingsmenu()
                    
                elif pos[0] in range(50,560) and pos[1] in range(490,585):
                    achievements()

                elif pos[0] in range(534,600) and pos[1] in range(15,73):
                    quitgame()
                    q=True
                
#funtion for the game running in offline 2 player mode
if __name__=="__main__":
    mainmenu(images)
