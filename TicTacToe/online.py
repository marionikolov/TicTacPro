from main import *
from logic import *
import socket, select, pickle, logging
from subprocess import call

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

def online(turn, images, host, port):
    call("dir", shell=True)
    screen = pygame.display.set_mode((610, 650))
    pygame.mixer.music.play(-1)
    screen.blit(images[0], (0, 0))
    used = [7, 8, 9, 4, 5, 6, 1, 2, 3]
    pygame.display.flip()
    count = 0
    isgamewon = (False, 9)
    
    try:
        gamecli = GameClient(host, port)
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
                # elif mousclick

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
                pass

            if count == 9:
                break
        #######
        if isgamewon:
            if turn:
                winner="1"
                achievements("won")
            else:
                winner="2"
                achievements("lost")
            print("The Winner is Player {0}!".format(winner)) 
        else:
            losersound.play()
            achievements("draw")
            print("No One Won!")
        pygame.mixer.music.fadeout(2000)
        time.sleep(2)
    finally:
        gamecli.shutdown()

if __name__=="__main__":
    online(True, images, "localhost", 12341)
