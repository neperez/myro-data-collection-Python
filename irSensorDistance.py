# Nicolas Perez
# Data collection program for a myro robot

from myro import*
import string

FILE_LOCATION_HOME = "C:\Users\Nick\Desktop\scribbler\IRSensors\data.txt"
FILE_LOCATION_LAB = "T:\Research\IRSensor\Values\data.txt"


def computeAverage(delayTime):
    count = 0
    sumOfSignals = 0
    while timeRemaining(delayTime):
        x = getObstacle("center")
        count += 1
        sumOfSignals += x
    average =  sumOfSignals / count
    return average

def setFileLocation():
    location = raw_input("Test location?:([l]ab, [h]ome): " )
    while  location != "l" and location != "h":
        location = raw_input("Invalid Entry.  Enter letter \'l\' for lab or letter \'h\' for home: " )
    if location == "l":
        filelocation = FILE_LOCATION_LAB
        setVolume(1)
    else:
        filelocation = FILE_LOCATION_HOME
        setVolume(0)
    return filelocation

def setFtype():
    ftype = raw_input("Choose attribute:([r]ead, [w]rite, [a]ppend): ")
    while ftype != "r" and ftype != "w" and ftype != "a":
        ftype = raw_input("Invalid Entry.  Enter letter \'r\' for read, letter \'w\' for write, or \'a\' for append: ")
    return ftype

def performTest(loopNumber):
    filelocation = setFileLocation()
    ftype = setFtype()
    delayTime = int(raw_input("Enter delay time for the getObstacle() sensors: "))
    outfile = open(filelocation, ftype)
    cycle = 0
    try:
        p0 = int(raw_input("Enter starting distance: "))
        p2 = int(raw_input("Enter the constant displacement distance: "))
        for _ in range(loopNumber):
            cycle += 1
            outfile.write(" %d " %cycle)
            p1 = p0
            print "The next distance is: ", p1
            raw_input("Press enter to start a new cycle <enter>")
            print "Cycle".rjust(50), cycle

            while p1 > 0:
                print "The current distance is = ", p1
                average = computeAverage(delayTime)
                print "The average is ", average
                outfile.write(" %d " %p1)
                outfile.write(" %d " %average)
                outfile.write("\n\n")
                beep(.2, 880)

                if p1 > 0:
                    raw_input("Move the robot manually, then press enter to continue <enter>")
                    p1 -= p2
                else:
                    continue
            print "\n"
            outfile.write("\n")
        print "End of cycle".rjust(50)
        outfile.close()
    except KeyboardInterrupt, SyntaxError:
        outfile.close()
        
        print "\nLoop canceled."
            
