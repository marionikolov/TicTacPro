from main import *
from logic import *
from achievements import *
import random
import time

def AIwinNext(used): #This code checks if the computer can win the next move
    for i in range(len(used)):
        if used[i] != "x" or used[i] != "o":
            oldi = used[i]
            used[i] = "o"
            isgamewoncheck = gamewon(used)
            used[i] = oldi
            if isgamewoncheck:
                if i == 7:
                    return (10,10)
                elif i == 8:
                    return (210,400)
                elif i == 9:
                    return (410,600)
                elif i == 4:
                    return (10,200)
                elif i == 5:
                    return (210,400)
                elif i == 6:
                    return (410,600)
                elif i == 1:
                    return (10,200)
                elif i == 2:
                    return (210,400)
                elif i == 3:
                    return (410,600)
            else:
                return None

def AIblockNext(used): #This checks if the player could win the next move, the computer will block them
    for i in range(len(used)):
        if used[i] != "x" or used[i] != "o":
            oldi = used[i]
            used[i] = "x"
            isgamewoncheck = gamewon(used)
            used[i] = oldi
            if isgamewoncheck:
                if i == 7:
                    return (10,10)
                elif i == 8:
                    return (210,400)
                elif i == 9:
                    return (410,600)
                elif i == 4:
                    return (10,200)
                elif i == 5:
                    return (210,400)
                elif i == 6:
                    return (410,600)
                elif i == 1 :
                    return (10,200)
                elif i == 2:
                    return (210,400)
                elif i == 3:
                    return (410,600)
            else:
                return None

def offline1p(difficulty, turn, images):
    """runs the offline 1 player iteration of the game"""
    screen=pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    screen.blit(images[0],(0,0))
    used=[7,8,9,4,5,6,1,2,3]
    pygame.display.flip()
    count=0
    isgamewon=(False,9)
    while count<9 and not isgamewon[0]:
        ev = pygame.event.get()
        for event in ev:
            if turn:
                # user move
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicksound.play()
                    valid=validmove(pos,used)
                    if valid:
                        drawbox(turn,pos,used,images)
                        isgamewon=gamewon(used)
                        count+=1
                        if isgamewon[0]:
                            drawline(isgamewon[1],turn,images)
                            break
                        turn=not turn
                    else:
                        print("That is not a valid move.")
                        nosound.play()
            elif not turn:
                # AI's move
                if difficulty == "easy":
                    pos = (random.randint(10,600), random.randint(10,600))
                elif difficulty == "medium":
                    pos = None
                    while pos is None:
                        pos = AIwinNext(used)
                        pos = AIblockNext(used)
                        pos = (random.randint(10,600), random.randint(10,600))
                elif difficulty == "hard":
                    #add code here, V
                    #This code checks if the computer can win the next move
                    for i in range(len(used)):
                        if used[i] != "x" or used != "o":
                            oldi = used[i]
                            used[i] = "o"
                            isgamewon = gamewon(used)
                            if isgamewon:
                                if i == 7:
                                    pos = (10,10)
                                elif i == 8:
                                    pos = (210,400)
                                elif i == 9:
                                    pos = (410,600)
                                elif i == 4:
                                    pos = (10,200)
                                elif i == 5:
                                    pos = (210,400)
                                elif i == 6:
                                    pos = (410,600)
                                elif i == 1 :
                                    pos = (10,200)
                                elif i == 2:
                                    pos = (210,400)
                                elif i == 3:
                                    pos = (410,600)  
                                drawbox(turn,pos,used,images)
                            else:
                                used[i] = oldi
                    
                    #This checks if the player could win the next move, the computer will block them
                    for i in range(len(used)):
                        if used[i] != "x" or used != "o":
                            oldi = used[i]
                            used[i] = "x"
                            isgamewon = gamewon(used)
                            if isgamewon:
                                if i == 7:
                                    pos = (10,10)
                                elif i == 8:
                                    pos = (210,400)
                                elif i == 9:
                                    pos = (410,600)
                                elif i == 4:
                                    pos = (10,200)
                                elif i == 5:
                                    pos = (210,400)
                                elif i == 6:
                                    pos = (410,600)
                                elif i == 1 :
                                    pos = (10,200)
                                elif i == 2:
                                    pos = (210,400)
                                elif i == 3:
                                    pos = (410,600)
                                drawbox(turn,pos,used,images)
                            else:
                                used[i] = oldi
                            
                    #The computer will check if the coners are free, it will take the corners
                    for i in [1,3,7,9]:
                        if used[i] != "x" or used != "o":
                            oldi = used[i]
                            used[i] = "o"
                            isgamewon = gamewon(used)
                            if isgamewon:
                                if i == 7:
                                    pos = (10,10)
                                elif i == 9:
                                    pos = (410,600)
                                elif i == 1 :
                                    pos = (10,200)
                                elif i == 3:
                                    pos = (410,600)
                                drawbox(turn,pos,used,images)
                            else:
                                used[i] = oldi

                    #This code allows the computer to check if the centre is free, it will take it
                    for i in [5]:
                        if used[i] != "x" or used != "o":
                            oldi = used[i]
                            used[i] = "o"
                            isgamewon = gamewon(used)
                            if isgamewon:
                                if i == 5:
                                    pos = (210,400)
                                drawbox(turn,pos,used,images)
                            else:
                                used[i] = oldi
                    print("hard")
                valid=validmove(pos,used)
                if valid:
                    clicksound.play()
                    drawbox(turn,pos,used,images)
                    isgamewon=gamewon(used)
                    count+=1
                    if isgamewon[0]:
                        drawline(isgamewon[1],turn,images)
                        break
                    turn=not turn
                else:
                    pass    
    if isgamewon:
        if turn:
            winner="1"
            print("The Winner is Player {0}!".format(winner))
            time.sleep(2)
            achievements("won")
        else:
            winner="2"
            print("The Winner is Player {0}!".format(winner))
            time.sleep(2)
            achievements("lost")
    else:
        losersound.play()
        print("No One Won!")
        time.sleep(2)
        achievements("draw")
    pygame.mixer.music.fadeout(2000)
    time.sleep(2)
    

if __name__=="__main__":
    offline1p("medium",True,images)
