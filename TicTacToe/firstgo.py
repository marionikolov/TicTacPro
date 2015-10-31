from main import *
from logic import *
import random
def chooseturn():
    #someones doing questions for this i think put it here :) and return boolean (true false)
    #true for player one, false for player 2
    #you can do what you want with it it's only for 2 player modes
    #you can use all the other logic code for stuff :)
    #you might also need to work out how to take in the online version for the choice as well
    winner=random.choice([True,False])
    return winner

if __name__=="__main__":
    chooseturn()
