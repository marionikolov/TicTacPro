"""
============================== TicTacPro ==============================
FILE: TicTacProLauncher.py
MODIFIED: 15/11/2015
STATUS: Complete
FILE DESCRIPTION:
the TicTacToeLauncher.py file is the bootstrap for the game, it is used to get
the server and port if you wish to launch the online version of the game.
"""

import os, time, sys

def valYN(prompt):
    while True:
        value = input(prompt).upper()
        if value not in ["Y", "N"]:
            print("Please enter Y or N according to your answer.")
            continue
        else:
            return value

def valhost(prompt):
    while True:
        value = input(prompt)
        if " " in value:
            print("Host cannot contain spaces.")
            continue
        else:
            return value

def valport(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except ValueError:
            print("Insert numbers only.")
            continue
    return str(value) # Convert to string in order to pass as sys argument.

def startGame(host, port):
        if sys.version_info[0] < 3:
            try:
                os.system("python3 main.py " + host + " " + port) # If the computer has both Python 2 and Python 3 installed, this will start the game under Python 3.
            except:
                raise OSError("Please install Python 3 to play the game.")
        elif sys.version_info[0] == 3:
            os.system("main.py " + host + " " + port)

if __name__ == "__main__":
    print("=========================== Welcome to TicTacPro! ===========================")
    print("We are preparing the TicTacPro GUI for you.")
    ans1 = valYN("Before we start, we need to know whether you will want to play online. (Y/N)")
    if ans1 == "Y":
        print()
        print("In order to play in online mode please provide the host name and the port number you will be connecting to.")
        host = valhost("Host: ")
        port = valport("Port: ")

        print()
        print("TicTacPro will now initiate with enabled online multiplayer on host " + host + " and port " + port)
        time.sleep(3)
        startGame(host, port)
    elif ans1 == "N":
        print("You have chosen to not play online during this session.")
        print("If you choose the online mode from the main menu, an exception will be raised.")
        startGame("no", "0")
