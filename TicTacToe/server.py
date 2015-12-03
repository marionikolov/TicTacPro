"""
============================== TicTacPro ==============================
FILE: server.py
MODIFIED: 23/11/2015
STATUS: debug
FILE DESCRIPTION:
The server.py file adds the functionality of playing multiplayer online games on a local network.
Events during the execution of the file will be logged to events.log.
USAGE:
The server.py file has to reside on the server computer to which clients will connect.
"""

import socket, select, logging

"""
CLASS NAME: servergo()
CLASS DESCRIPTION:
Initializes the server needed to host an online multiplayer game of TicTacPro. Makes use of a TCP/IP sockets for the client-server connection.
This server acts as a bridge between the two clients, i.e. sends information from one to the other. No actions are performed on the data while travelling to and from the server.
"""
class servergo():
    """
    FUNCTION NAME: __init__
    PARAMETERS: 2
                ipaddr (string; optional; defaults to "localhost"): the server IP address which will host client connections
                port (integer; optional; defaults to 12341): the socket port which clients will connect to
    FUNCTION DESCRIPTION:
    Initializes the server connection with the default parameters unless others are provided. 
    """
    def __init__(self, ipaddr = "localhost", port = 12341):
        self.connections = []   # Declare a list that will hold all connections.
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create an IPv4 TCP socket.
        self.server.bind((ipaddr, port))    # Bind the socket to the provided host and port.
        self.server.listen(2)   # Accept a maximum of 2 client connections.
        print("TicTacPro server started on host " + str(socket.gethostbyname(socket.gethostname())) + " and port " + str(port)) # Informs the user of the host IP address and the port number. Clients must use this data to connect in order to play multiplayer online.
        print("")

    """
    FUNCTION NAME: shutdown()
    PARAMETERS: 0
    FUNCTION DESCRIPTION:
    Closes the connection to each client and the completely shuts down the server. No connection to the server can be established afterwards.
    """
    def shutdown(self):
        for conn in self.connections:
            conn.close()
        self.server.shutdown(1)
        self.server.close()

    """
    FUNCTION NAME: play()
    PARAMETERS: 0
    FUNCTION DESCRIPTION:
    Accepts new connections and appends them to the connection list (self.connections).
    Transfers information from one client to the other.
    """
    def play(self):
        read, write, error = select.select(self.connections+[self.server], self.connections, self.connections, 0) # Get the list of socke
        
        for conn in read:
            if conn is self.server: # Handle new clients connecting to the server.
                c, addr = conn.accept()
                self.connections.append(c)
                print("New client connected: " + str(addr))
            else:
                data = conn.recv(1024)
                if not data: # If no data is received, the client has disconnected. Close the connection and end the online game.
                    conn.close()
                    self.shutdown()
                elif data: # If data is received, send it to the other client.
                    for client in self.connections:
                        if client != conn:
                            try:
                                client.send(data)
                            except Exception as e:
                                print("Could not send to " + str(conn))
                                logging.error("Could not send to " + str(conn) + " Exception details: " + str(e))

if __name__ == "__main__":
    logging.basicConfig(filename="events.log", format="%(asctime)s [server.py] %(message)s", datefmt="%Y/%m/%d %I:%M:%S %p")    # Event logging configuration.
    try:
        server = servergo()
        while True: # Keep server alive.
            server.play()
    except Exception as e:
        logging.exception(str(e))
    finally:
        server.shutdown()
