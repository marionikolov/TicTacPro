import pickle

def achievereset():
        #resets the acheivements file
	f = open("achievements.pickle", "wb")
	stats = [0,0,0,0,0]
	pickle.dump(stats,f)
	f.close()

if __name__ == "__main__":
	achievereset()
