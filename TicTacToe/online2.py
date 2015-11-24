from main import *
from logic import *
import socket, select, pickle

class GameClient():
    def __init__(self, host="localhost", port=12341):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.messages = []
        self.recvmessages = []

    def shutdown(self):
        self.server.shutdown(1)
        self.client.close()

    def send_message(self, msg):
        msg = pickle.dumps(msg)
        self.messages.append(msg)

    def recv_message(self):
        if self.recvmessages:
            #buf = pickle.loads(self.recvmessages[0])
            #del  # try doing it with pop instead
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

def online(turn, images):
    screen=pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    screen.blit(images[0],(0,0))
    used=[7,8,9,4,5,6,1,2,3]
    pygame.display.flip()
    count=0
    isgamewon=(False,9)
    try:
        gamecli = GameClient()
        while True:
            gamecli.poll()
            #ev = pygame.event.clear()
            ev = pygame.event.get()
            #########
            for event in ev:
                #######
                if turn:
                    # local user move
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        clicksound.play()
                        valid = validmove(pos, used)
                        if valid:
                            gamecli.send_message(pos)
                            drawbox(turn, pos, used, images)
                            isgamewon = gamewon(used)
                            count += 1
                            # chech whether this is not redundant
                            if isgamewon[0]:
                                drawline(isgamewon[1], turn, images)
                                break
                            turn=not turn
                        else:
                            print("That is not a valid move.")
                            nosound.play()
                #######
                elif not turn:
                    pos = gamecli.recv_message()
                    if pos:
                        clicksound.play()
                        drawbox(turn, pos, used, images)
                        isgamewon = gamewon(used)
                        count += 1
                        if isgamewon[0]:
                            drawline(isgamewon[1],turn,images)
                            break
                        turn=not turn
            #######
        if isgamewon:
            if turn: winner="1"
            else: winner="2"
            print("The Winner is Player {0}!".format(winner)) 
        else: losersound.play(),print("No One Won!")
        pygame.mixer.music.fadeout(2000)
        time.sleep(2)
    finally:
        gamecli.shutdown()
        
if __name__=="__main__":
    online(False, images)
