from main import *
from logic import *
import random

def AIwinNext(used): #This code checks if the computer can win the next move
    for i in range(len(used)):
        if used[i] != "x" and used[i] != "o":
            oldi = used[i]
            used[i] = "o"
            isgamewoncheck = gamewon(used)
            used[i] = oldi
            if isgamewoncheck[0]:
                if oldi == 7:
                    return (10,10)
                elif oldi == 8:
                    return (210,10)
                elif oldi == 9:
                    return (410,10)
                elif oldi == 4:
                    return (10,210)
                elif oldi == 5:
                    return (210,210)
                elif oldi == 6:
                    return (410,210)
                elif oldi == 1:
                    return (10,410)
                elif oldi == 2:
                    return (210,410)
                elif oldi == 3:
                    return (410,410)
    return None

def AIblockNext(used):
    for i in range(len(used)):
        if used[i] != "x" and used[i] != "o":
            oldi = used[i]
            used[i] = "x"
            isgamewoncheck = gamewon(used)
            used[i] = oldi
            if isgamewoncheck[0]:
                if oldi == 7:
                    return (10,10)
                elif oldi == 8:
                    return (210,10)
                elif oldi == 9:
                    return (410,10)
                elif oldi == 4:
                    return (10,210)
                elif oldi == 5:
                    return (210,210)
                elif oldi == 6:
                    return (410,210)
                elif oldi == 1:
                    return (10,410)
                elif oldi == 2:
                    return (210,410)
                elif oldi == 3:
                    return (410,410)
    return None

def AItakeCorner(used):
    corners = [0, 2, 6, 8]
    random.shuffle(corners)
    for i in corners:
        if used[i] != "x" and used[i] != "o":
            if used[i] == 7:
                return (10,10)
            elif used[i] == 9:
                return (410,10)
            elif used[i] == 1:
                return (10,410)
            elif used[i] == 3:
                return (410,410)
    return None

def AItakeCentre(used):
    if used[4] != "x" and used[4] != "o":
        return (210,210)

def AItakeRandom(used):
    unused = []
    for i in used:
        if i != "x" and i != "o":
            unused.append(i)
    square = random.choice(unused)
    if square == 7:
        return (10,10)
    elif square == 8:
        return (210,10)
    elif square == 9:
        return (410,10)
    elif square == 4:
        return (10,210)
    elif square == 5:
        return (210,210)
    elif square == 6:
        return (410,210)
    elif square == 1:
        return (10,410)
    elif square == 2:
        return (210,410)
    elif square == 3:
        return (410,410)