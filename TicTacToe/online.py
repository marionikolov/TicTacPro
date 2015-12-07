"""
============================== TicTacPro ==============================
FILE: Online.py
MODIFIED: 15/11/2015
STATUS: Complete
FILE DESCRIPTION:
the Online.py file is the online version of the tictactoe game, it allows
communication between 2 machines through a server, which sends commands for
not only board positions but also the chat, which allows text communication
between the 2 clients
"""
from main import *
from logic import *
from chat import *
from firstgo import *
import socket, select, pickle, logging

class GameClient():
    def __init__(self, host="localhost", port=12341):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.messages = []
        self.recvmessages = []

    def shutdown(self):
        self.client.shutdown(1)
        self.client.close()

    def send_message(self, msg):
        msg = pickle.dumps(msg)
        self.messages.append(msg)

    def recv_message(self):
        if self.recvmessages:
            return pickle.loads(self.recvmessages.pop(0))
        
    def poll(self):
        read, write, error = select.select ( [self.client], [self.client], [self.client], 0 )

        for conn in read:
            newmsg = self.client.recv(1024)
            if newmsg:
                self.recvmessages.append(newmsg)

        for conn in write:
            for i in self.messages:
                conn.send(i)
                self.messages.remove(i)

def online(images, host, port):
    used = [7, 8, 9, 4, 5, 6, 1, 2, 3]
    count = 0
    isgamewon = (False, 9)
    chat=[]
    displaystring=""
    try:
        gamecli = GameClient(host, port)
        
        myturn = None
        while True:
            if myturn is None:
                myturn = askquestion()
                gamecli.send_message(myturn)
            gamecli.poll() # Send and receive messages between opponents.
            newmsg = gamecli.recv_message()
            if myturn is not None and newmsg is not None:
                if myturn == newmsg:
                    print("Both players answered correctly. Try again.")
                    time.sleep(2)
                    myturn = None
                else:
                    turn = myturn
                    break
        screen = pygame.display.set_mode((900, 650))
        pygame.mixer.music.play(-1)
        screen.blit(images[0], (0, 0))
        pygame.display.flip()

        while True:
            ev = pygame.event.get()
            for event in ev:
                if turn and event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    clicksound.play()
                    valid = validmove(pos, used)
                    if valid:
                        gamecli.send_message(pos)
                        drawbox(turn, pos, used, images)
                        isgamewon = gamewon(used)
                        count += 1
                        if isgamewon[0]:
                            drawline(isgamewon[1], turn, images)
                            break
                        turn = not turn
                    else:
                        print("That is not a valid move.")
                        nosound.play()

                elif event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        if displaystring!="":
                            chat.insert(0,("You",displaystring))
                            gamecli.send_message(displaystring)
                        displaystring=""
                        drawlist(chat)
                    else:   
                        displaystring,chat=chatinput(event.key,displaystring,chat)
                    
                elif event.type == pygame.QUIT:
                    quitgame()
                    
            gamecli.poll() # Send and receive messages between opponents.
            newmsg = gamecli.recv_message()
        
            if not turn and isinstance(newmsg, tuple):
                drawbox(turn, newmsg, used, images)
                clicksound.play()
                isgamewon = gamewon(used)
                count += 1
                if isgamewon[0]:
                    drawline(isgamewon[1], turn, images)
                    break
                turn = not turn

            if isinstance(newmsg, str):
                chat.insert(0,("Opponent",newmsg))
                drawlist(chat)
            if count == 9:
                break

        if isgamewon:
            if turn:
                print("You won! Congratulations!")
                time.sleep(2)
                achievements("won")
            else:
                print("Better luck next time!")
                time.sleep(2)
                achievements("lost")
        else:
            losersound.play()
            print("The game is a draw!")
            time.sleep(2)
            achievements("draw")
        pygame.mixer.music.fadeout(2000)
        time.sleep(2)
    finally:
        gamecli.shutdown()

if __name__=="__main__":
    online(images, "localhost", 12341)
