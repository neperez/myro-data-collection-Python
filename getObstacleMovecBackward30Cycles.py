#Nicolas Perez
#Data collection for myro robot

from myro import*

def begin(timeLimit, rSpeed):

    raw_input("move robot to starting point, then press enter <enter>")
    try:  
        #initialize necessary components
        fileString = """T:\Research\ResearchMay2011\data\\textdata\\trial7\data""" + str(rSpeed) +"speed.txt"
        outfile = open( fileString, "w" )
        curCycle = 1
        cycleNumber = 30 
        
        #write header text
        outfile.write( "Robot Speed: %f" %rSpeed )
        outfile.write( "\n" )
        outfile.write( "Time limit: %f" %timeLimit )
        outfile.write( "\n" )
        while curCycle <= cycleNumber:
            beep(.1, 840)
            #initialize variables for current loop
            curTimeInterval = 0
            #current cycle header
            print "Cycle is: ", curCycle
            outfile.write( "Cycle %d" %curCycle )
            outfile.write( "\n" )
            startTime = currentTime()
            forward(rSpeed)
            add deltaTime = currentTime() - startTime
            while curTimeInterval < timeLimit:
                x = getObstacle( "center" )
                nowTime = currentTime()
                curTimeInterval = nowTime - startTime
                print x, "\t", curTimeInterval
                outfile.write( "\n" )
                outfile.write( " %d " %x )
                outfile.write( "%f " %curTimeInterval )
            stop()
            beep(.1, 900)
            distOver = raw_input( "End distance from 20 inches: " )
            outfile.write( "\n" )
            outfile.write( "End distance from 20 inches: %s" %distOver )
            outfile.write( "\n" )
            outfile.write("Difference in time: %f" %deltaTime)
            outfile.write( "\n" )
            raw_input( "Move robot to starting point then press enter to start new cycle <enter>" )
            wait(.5)
            curCycle += 1
        outfile.close()
        print "Cycles completed."
    except KeyboardInterrupt, SyntaxError:
        outfile.close()
        print "program terminated"

        
        
