"""
============================== TicTacPro ==============================
FILE: chat.py
MODIFIED: 27/11/2015
STATUS: Complete
FILE DESCRIPTION:
    The chat.py file contains all the functions relating to displaying the chat and
    input and the chat list.
    
USAGE:
This is a client chat display and input management function.
"""
from main import *
from logic import *

def main():
    screen=pygame.display.set_mode((900, 650))
    pygame.draw.rect(screen, (0,0,0), [610, 0, 300, 700], 0)
    chat=[]
    displaystring=""
    turn=True
    while True:
        #how i get mouse clicks this is event driven programming
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                displaystring,chat=chatinput(event.key,displaystring,chat)

def chatinput(eventkey,displaystring,chat):
    #this function runs when a key is presed, and decides what to do with it
    
    if eventkey in range(97,123) or eventkey in range(48,58):
        #these ranges are a-z and 0-9, as it is the ascii value it is simple to
        #convert the number to a letter or number
        displaystring+=str(chr(eventkey))
    
    elif eventkey == 13:
        #when the enter key is pressed, sends the message to the server and also
        #it clears the display string and adds it to the chat list, then draws the chat
        if displaystring!="":
            chat.insert(0,("You",displaystring))
            sendmsg=displaystring
        displaystring=""
        drawlist(chat)
        
    elif eventkey == 32:
        #whhen the space key is pressed a blank space in inserted into the displaystring
        displaystring+=" "
    
    elif eventkey == 8:
        #when the backspace key is pressed the last letter in the displaystring is removed
        displaystring=displaystring[:-1]
        
    #display the current input message
    showinput(displaystring)
    return displaystring,chat

def showinput(string):
    string=(": "+string)
    #covers up any previous stuff on the screen 
    pygame.draw.rect(screen, (0,0,0), [610, 600, 300, 700], 0)
    #draws texts on screen
    font = pygame.font.Font(None, 16)
    text = font.render(string, 4, (255, 255, 255))
    screen.blit(text, (620,610))
    #updates screen to show new changes
    pygame.display.flip()
    
def drawlist(chat):
    #set the bottom height of the screen
    y=540
    #deletes the oldest message in the chat after it gets to 14 messages
    if len(chat)>14: del chat[-1]   
    pygame.draw.rect(screen, (0,0,0), [610, 0, 300, 700], 0)
    for each in chat:
        #generates the output string
        each=(str(each[0]) +": " + str(each[1]))
        #decides how to handle printing out the statement, if it will fit on one line or not
        if len(each)<47:
            #prints the string out at the y coord
            font = pygame.font.Font(None, 16)
            chatstuff = font.render(each, 4, (255, 255, 255))
            screen.blit(chatstuff, (620,y))
            #moves the y coord down to accomodate the next message
            y-=40
            
        elif len(each)>120:
            #word limit
            print("Too long to display!")
            
        else:
            #smaller recursive loop like the one above for multi line messages
            y2=y
            y-=40
            while len(each)!=0:
                #takes one lines worth of code from the each string
                line=each[:40]
                each=each[40:]
                font = pygame.font.Font(None, 16)
                chatstuff = font.render(line, 4, (255, 255, 255))
                screen.blit(chatstuff, (620,y2))
                #moves it down slightly lower to give a multiline effect
                y2+=10
            
        pygame.display.flip()
if __name__=="__main__":
    main()
    
