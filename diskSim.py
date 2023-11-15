import sys

#Notes
#Turn this file into an executable before submitting

def main():

    if len(sys.argv) <2 or len(sys.argv) >3:
        print("Usage: python diskSim.py INITIAL_POSITION OPTIONAL:[ACCESS_SEQUENCE_FILE]")
        return
    
    initialPosition = int(sys.argv[1])
    accessSequenceFile = None
    try:
        if len(sys.argv) == 3:
            open(sys.argv[2], "r")
            accessSequenceFile = sys.argv[2]
    except:
        print("Error: " + "\"" + sys.argv[2] + "\"" + " not found" )
        return
   

    print(accessSequenceFile)

    print("Hello World!")


if __name__ == "__main__":
    main()