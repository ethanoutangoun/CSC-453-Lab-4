import sys
import random

#Notes
#Turn this file into an executable before submitting


#Function to generate a random sequence of tracks to access from 0-4999
def generateRandomTracks():
    l = []
    for i in range(1000):
        l.append(random.randint(0,4999))
    return l


def main():

    if len(sys.argv) <2 or len(sys.argv) >3:
        print("Usage: python diskSim.py INITIAL_POSITION OPTIONAL:[ACCESS_SEQUENCE_FILE]")
        return
    
    initialPosition = int(sys.argv[1])
    accessSequenceFile = None
    accessSequence = []
    try:
        if len(sys.argv) == 3:
            open(sys.argv[2], "r")
            accessSequenceFile = sys.argv[2]
    except:
        print("Error: " + "\"" + sys.argv[2] + "\"" + " not found" )
        return
   
    if initialPosition <-4999 or initialPosition >4999:
        print("Error: Initial position must be between -4999 and 4999")
        return
    


    if accessSequenceFile == None:
        accessSequence = generateRandomTracks()

    for num in accessSequence:
        print(num)
    



if __name__ == "__main__":
    main()