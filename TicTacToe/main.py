#init stuff
import pygame, math, sys, time, os
from os.path import dirname, realpath, abspath
pygame.init()
#game wide initalistion, if its specific to one mode then do it in that games function
pygame.image.load("icon.png")
screen=pygame.display.set_mode((610, 650))
clock = pygame.time.Clock()
rick=pygame.image.load("rick.png")
board=pygame.image.load("board.png")
pygame.display.set_caption("TicTacPro Game","TicTacPro")
#all sound files from sounddogs.com royalty free and some editied by me
special=pygame.mixer.Sound("special.wav")
pygame.mixer.music.load("music.wav")
clicksound=pygame.mixer.Sound("click.wav")
winsound=pygame.mixer.Sound("win.wav")
losersound=pygame.mixer.Sound("loser.wav")
nosound=pygame.mixer.Sound("no.wav")

#shared code for game logic etc
from offline2p import *
from offline1p import *
from online import *
from achievements import *
from settings import *
from firstgo import *

def mainmenu():
    #needs a GUI, just the concept
    #1 - online
    #2 - offline1p
    #3 - offline2p
    #4 - achievements
    #5 - settings
    q=False
    while not q:
        while True:
            choice=input("What would you like to do? ")
            if choice in ["1","2","3","4","5","0"]:
                break
            else:
                print("That's not an option")
        if choice=="1":
            whosturn=chooseturn()
            online(whosturn)
        elif choice=="2":
            whosturn=random.choice([True, False])
            offline1p("easy",whosturn)
        elif choice=="3":
            whosturn=chooseturn()
            offline2p(whosturn)
        elif choice=="4":
            achievements()
        elif choice=="5":
            settings()
        elif choice=="0":
            print("Goodbye!")
            time.sleep(1)
            q=True
        else:
            print("You broke it somehow good job!")
        
#funtion for the game running in offline 2 player mode
if __name__=="__main__":
    mainmenu()
