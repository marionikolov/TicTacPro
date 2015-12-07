from main import *
from logic import *

def offline2p(images):
    """runs the offline 2 player iteration of the game"""
    screen=pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    screen.blit(images[0],(0,0))
    used=[7,8,9,4,5,6,1,2,3]
    pygame.display.flip()
    count=0
    turn = True
    isgamewon=(False,9)
    while count<9 and not isgamewon[0]:
        if turn:
            print("It is Player 1's turn.")
        else:
            print("It is Player 2's turn.")
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
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
                    nosound.play()
                    print("That is not a valid move.") 
            elif event.type == pygame.QUIT:
                quitgame()

    if isgamewon[0]:
        if turn:
            winner = "1"
            print("The winner is Player {0}!".format(winner))
        else:
            winner = "2"
            print("The winner is Player {0}!".format(winner))
    else:
        losersound.play()
        print("The game is a draw!")
        time.sleep(2)
        achievements("draw")
    pygame.mixer.music.fadeout(2000)
    time.sleep(2)
    
if __name__=="__main__":
    offline2p(images)
