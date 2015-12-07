"""
============================== TicTacPro ==============================
FILE: Acheivements.py
MODIFIED: 15/11/2015
STATUS: Complete
FILE DESCRIPTION:
The achievements.py file is used for loading and saving the achievements stats to a binary file for
a more permantant as it means the variables can be tranferred between instances of the game running
rather than being local to each instance of the program being run.
USAGE:
Used for saving and loading from files
"""

from main import *
from logic import *
import pickle

def achievereset():
    #resets the acheivements file
    f = open("achievements.pickle", "wb")
    stats = [0,0,0,0,0]
    pickle.dump(stats,f)
    f.close()

def achievements(res):
    #loads the stats from a local file
    f = open("achievements.pickle","rb")
    stats = pickle.load(f)
    f.close()
    #1-games played, 2-games won 3-games lost 4 - games draw 5 - level
    if res == "won":
        #ups the stats
        stats[0]+=1
        stats[1]+=1
        stats[4]+=1
        print("You are level " + str(stats[4]))
    elif res == "lost":
        if int(stats[4]) >1 :
            stats[0]+=1
            stats[2]+=1
            stats[4]-=0.5
            print("You are level "+ str(stats[4]))
        if int(stats[4]) <= 1:
            stats[0]+=1
            print("You are still on level 1!")
    elif res == "draw":
        stats[0]+=1
        stats[3]+=1
        stats[4]+=0.5
        print("You are level " + str(stats[4]))
    #closes the stats file
    f = open("achievements.pickle","wb")
    pickle.dump(stats, f)
    f.close()

def achievementsview():
    #clears the last event and sets up the window for the viewing the achievements
    pygame.event.clear()
    screen=pygame.display.set_mode((610, 650))
    achievementsmenu=pygame.image.load("images/menu/settings/achievementsmenu.png")
    screen.blit(achievementsmenu,(0,0))
    #loads the achievements
    f = open("achievements.pickle","rb")
    stats = pickle.load(f)
    f.close()
    #prints them out in the corresponding locations
    print("Games played ...................................... " + str(stats[0]),70,140)
    print("Games won .......................................... " + str(stats[1]),70,200)
    print("Games lost ........................................... " + str(stats[2]),70,260)
    print("Games drawn ...................................... " + str(stats[3]),70,320)
    print("You are level " + str(stats[4]),200,380)
    
    q=False
    while not q:  
        pygame.display.flip()
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                #checks for the back button being pressed
                pos = pygame.mouse.get_pos()
                if pos[0] in range(23,204) and pos[1] in range(540,600):
                    return None

if __name__=="__main__":
    achievements("won")
