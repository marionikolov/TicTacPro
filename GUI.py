import pygame, math, sys, time, random
screen=pygame.display.set_mode((610, 610))
clock = pygame.time.Clock()
board=pygame.image.load("board.png")


def main():
    x=pygame.image.load('x.png')
    o=pygame.image.load('o.png')

    screen.blit(board,(0,0))
    used=[7,8,9,4,5,6,1,2,3]
    pygame.display.flip()
    turn=True
    count=0
    isgamewon=(False,9)
    while count<9 and not isgamewon[0]:
        ev = pygame.event.get()
        for event in ev:
            if turn:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    valid=validmove(pos,used)
                    if valid:
                        drawbox(o,x,turn,pos,used)
                        isgamewon=gamewon(used)
                        count+=1
                        print(isgamewon)
                        if isgamewon[0]:
                            print(isgamewon)
                            drawline(wincombo)
                            break
                        turn=not turn
                    else:
                        pass
                        print("no")
            elif not turn:
                posx = random.randint(10,600)
                posy = random.randint(10,600)
                pos = (posx, posy)
                valid=validmove(pos,used)
                if valid:
                    drawbox(o,x,turn,pos,used)
                    isgamewon=gamewon(used)
                    count+=1
                    print(isgamewon)
                    if isgamewon[0]:
                        print(isgamewon)
                        drawline(wincombo)
                        break
                    turn=not turn
                else:
                    pass
                    print("no")
                
    if isgamewon[1]:
        if turn: winner="1"
        else: winner="2"
        print("The Winner is Player {0}!".format(winner))
    else: print("It's ok it's the taking part that counts!")
    
    time.sleep(2)
    pygame.quit()

def gamewon(used):#fix
    if used[0]==used[1] and used[1]==used[2]: return (True,1)
    elif used[3]==used[4] and used[4]==used[5]: return (True,2)
    elif used[6]==used[7] and used[7]==used[8]: return (True,3)
    elif used[0]==used[3] and used[3]==used[6]: return (True,4)
    elif used[1]==used[4] and used[4]==used[7]: return (True,5)
    elif used[2]==used[5] and used[5]==used[8]: return (True,6)
    elif used[0]==used[4] and used[4]==used[8]: return (True,7)
    elif used[2]==used[4] and used[4]==used[6]: return (True,8)
    else: return (False,9)
    
    
def validmove(pos,used):
    
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
        
def drawbox(o,x,turn,pos,used):
    #box7
    if pos[0] in range(10,200) and pos[1] in range(10,200) and used :
        if turn:
            screen.blit(x,(10,10))
            used[0]="x"
        else:
            screen.blit(o,(10,10))
            used[0]="o"
    #box8        
    elif pos[0] in range(210,400) and pos[1] in range(10,200):
        if turn:
            screen.blit(x,(210,10))
            used[1]="x"
        else:
            screen.blit(o,(210,10))
            used[1]="o"
    #box9
    elif pos[0] in range(410,600) and pos[1] in range(10,200):
        if turn:
            screen.blit(x,(410,10))
            used[2]="x"
        else:
            screen.blit(o,(410,10))
            used[2]="o"
            
    #box4
    elif pos[0] in range(10,200) and pos[1] in range(210,400):
        if turn:
            screen.blit(x,(10,210))
            used[3]="x"
        else:
            screen.blit(o,(10,210))
            used[3]="o"
    #box5        
    elif pos[0] in range(210,400) and pos[1] in range(210,400):
        if turn:
            screen.blit(x,(210,210))
            used[4]="x"
        else:
            screen.blit(o,(210,210))
            used[4]="o"
    #box6
    elif pos[0] in range(410,600) and pos[1] in range(210,400):
        if turn:
            screen.blit(x,(410,210))
            used[5]="x"
        else:
            screen.blit(o,(410,210))
            used[5]="o"


            
    #box1
    elif pos[0] in range(10,200) and pos[1] in range(410,600):
        if turn:
            screen.blit(x,(10,410))
            used[6]="x"
        else:
            screen.blit(o,(10,410))
            used[6]="o"
    #box2        
    elif pos[0] in range(210,400) and pos[1] in range(410,600):
        if turn:
            screen.blit(x,(210,410))
            used[7]="x"
        else:
            screen.blit(o,(210,410))
            used[7]="o"
    #box3
    elif pos[0] in range(410,600) and pos[1] in range(410,600):
        if turn:
            screen.blit(x,(410,410))
            used[8]="x"
        else:
            screen.blit(o,(410,410))
            used[8]="o"
            
    #turn=not turn
    pygame.display.flip()
    return used


if __name__=="__main__":
    main()
