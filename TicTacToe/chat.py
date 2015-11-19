from main import *
screen=pygame.display.set_mode((900, 650))

def main():
    chat=[]
    turn=True
    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pass
        if turn:
            a=input(": ")
            chat.insert(0,("TotallyNotJiminy",a))
            drawlist(chat)
        else:
            b=input(": ")
            chat.insert(0,("PartyBoi 69",b))
            drawlist(chat)
        turn=not turn
def drawlist(chat):
    y=500
    if len(chat)>6: del chat[-1]
    pygame.draw.rect(screen, (0,100,120), [610, 0, 300, 700], 0)
    for each in chat:
        each=(str(each[0]) +": " + str(each[1]))
        if len(each)<40:
            font = pygame.font.Font(None, 16)
            chatstuff = font.render(each, 4, (255, 255, 255))
            screen.blit(chatstuff, (630,y))
            y-=80
        else:
            pass
##            bigmes=[]
##            while True:
##                each2=each
##                if len(each2)>40:
##                    each2=each[40:]
##                    each=each[:40]
##                    bigmes.append(each)
##                else:
##                    bigmes.append(each2)
##                    break
##            y2=y
##            for each in bigmes:
##                print(len(bigmes))
##                font = pygame.font.Font(None, 16)
##                chatstuff = font.render(each, 4, (255, 255, 255))
##                screen.blit(chatstuff, (630,y2))
##                y2+=5       
        pygame.display.flip()
if __name__=="__main__":
    main()
    
