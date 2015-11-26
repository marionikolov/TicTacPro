from main import *
from logic import *
import pickle
#0=number of games
#1=games won
#2=games lost
#3=games draw
#4=reputation

def achievements(res):
    #load
    pickle_in = open("doc.pickle","rb")
    stats=pickle.load(pickle_in)
    stats = [0,0,0,0,0]
    #achievements = {1:"Congratulations on your win. You are lever 1!", 2:"You are level 2"}
    if res == "won":
        stats[0]+=1
        stats[1]+=1
        stats[4]+=2
        print("Your level is " + str(stats[4]))
    elif res == "lost":
        stats[0]+=1
        stats[2]+=1
        stats[4]-=1
        if stats[4]<=0:
            print("You are still on level 1")
        else:
            print("You are on level " + str(stats[4]))
    
    elif res == "draw":
        stats[0]+=1
        stats[3]+=1
        stats[4]+=1
        print("You are on level " + str(stats[4]))

    #save
    pickle_out = open("doc.pickle","wb")
    pickle.dump(stats, pickle_out)
    pickle_out.close()
    
if __name__=="__main__":
    achievements("won")
