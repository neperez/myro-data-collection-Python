#Nicolas Perez
# Data collection for myro robot
from myro import*
import decimal



def begin(timeLimit, rSpeed):
    try:
        #initialize necessary components
        fileString = """T:\Research\ResearchMay2011\data\\textdata\\trial7\data""" + str(rSpeed) + "speed.txt"
        outfile = open(fileString, "w")
        timeInterval = 0
        deltaTime = 0
        outfile.write("speed: %f" %rSpeed)
        outfile.write("\n")
        outfile.write("time limit: %f" %timeLimit)
        outfile.write("\n")
        startTime = currentTime()
        forward(rSpeed)
        deltaTime = startTime - currentTime()
        while timeInterval < timeLimit:
            x = getObstacle("center")
            nowTime = currentTime()
            timeInterval = nowTime - startTime
            print x, "\t", timeInterval
            outfile.write("\n")
            outfile.write(" %d " %x)
            outfile.write("%f " %timeInterval)
        stop()
        distOver = raw_input("Enter distance from 19: ")
        outfile.write("\n")
        outfile.write("Distance from 19 inches: %s" %distOver)
        outfile.write("\n")
        outfile.write("Difference in start time is %f" %deltaTime)
        outfile.write("\n")
        totalDistance = 19
        adjustedDistance = totalDistance + float(distOver)
        outfile.close()
    except KeyboardInterrupt, SyntaxError:
        outfile.close()
        print "program terminated"
