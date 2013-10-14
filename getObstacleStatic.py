"""
Date:       04/30/2011

Program:    getobstacle program edit

Authors:    Nicolas Perez

Purpose:    To collect IR obstacle sensor readings from the Scribbler robot by manually
            moving the robot from 2 to 20 inches in 2 inch intervals.
            The sensor readings are collected for a certain period of time at each distance.
            The data is written to specified text file so it can be analysed.

Methods:    timeToComputeAverage() - computes average over a time duration.
            timer() - introduces a time delay in program excecution.
            readdata() - Parses data by distance and places into specified text files.
            main() - entry point for program.
"""

from myro import*

"""
Method:     timeToComputeAverage():

Purpose:    This method collects signals from the getObstacle sensor for an
            alloted time period t in seconds.  The signals are then averaged
            and returned to the caller.

Parameters: t - length of time to collect signals

Returns:    average - the average of the signals during the passed in time period.

Variables:  count -  the number of sensor readings taken during the time period.
            avgSum - the running sum of sensor values.
            x - a signal value read from the IR obstacle sensors.
            average - the average of the signals during the time period.
"""
def timeToComputeAverage( t ):
    count = 0
    avgSum = 0
    while timeRemaining( t ):
        x = getObstacle( "center" )
        count += 1
        avgSum += x
    average = avgSum / count
    return average

"""
Method:     timer():

Purpose:    To introduce a time delay in the program so the IR obstacles sensors can stablize.    

Parameters: seconds - The amount of time delay required.

Returns:    No return value used.

Variables:  count - For counting the seconds of the time delay.
            seconds - Tne duration of time to wait in seconds.            
"""
def timer( seconds ):
    count = 0
    print "\nPlease wait",
    # Number of seconds for sensors to stabilize
    while count < seconds:
        print ".",
        wait( 1 )
        count += 1
        
"""
Method:     readdata():

Purpose:    Separates data by distance into separate text files for later analysis.

Parameters: No parameters.

Returns:    No return values.

Variables:  initialSkipNumber -
            nextNumber -
            infile -
"""
def readdata():
    initialSkipNumber = 9
    nextNumber = 10
    infile = open("T:\Research\Cycles\data.txt","r")
    outfile = open("T:\Research\Cycles\inches_2.txt","w")

    def skip_lines( number ):
        for i in range( number ):
            infile.readline()

    skip_lines( initialSkipNumber )
    a = infile.readline()
    count = 0
    while count < 30:
        b = string.split( a )
        c = map( int, b )
        print c
        outfile.write( "%s \n" %c )
        for i in range ( nextNumber ):
            infile.readline()
        a = infile.readline()
        count += 1 
        
    infile.close()
    outfile.close()       
"""
Method:     main():

Purpose:

Parameters:

Returns:

Variables:

"""
def main():
    #Locate file pathway before beginning.
    filelocation = raw_input( "Input File e.g.(T:\Research\0.8_cycles\...: " )
    ftype = raw_input( "Input attribute\n[r] read, [w]write, [a]append (r,w, a):  " )
    loop=input( "Enter number of reiterations(loop): " )
    #Cancel out of loop after every cycle, or press CTRL+C to manually cancel loop
    t=input( "Enter duration for getObstacle() sensors:" )
    outfile = open( filelocation,ftype )
    cycle = 0
    p0= input( "Enter starting distance: " )
    p2 = input ( "Enter the constant displacement distance: " )
    try:

        for x in range( loop ):
            cycle += 1
            p1 = p0
            print
            print "*************************"
            print "       Cycle ",cycle,"   "
            print "*************************"
            print
            print
            raw_input( "***Press enter to start new cycle <enter>***" )
            print "Move the robot to distance", p1
            wait( 1 )
            while p1 >= 2:
                    #Number of seconds for sensors to stabilize
                    timer( 2 )
                    print
                    print "\nDistance = ", p1
                    average = timeToComputeAverage( t )
                    print "Average= ", average
                    outfile.write( "%d " %p1 )
                    outfile.write( "%d " %average )
                    beep( .2, 880 )
                    outfile.write( "\n" )
                    if p1 > 2:
                        p1 = p1 - p2
                        beep(.2,660)
                        print "\nMove robot to distance: ",p1
                        raw_input( "Press <enter> to continue\n" )
                    else:
                        p1 = 0
                        wait( 1 )
                        print
                        outfile.write( "\n" )
                        beep( .08,880 )
                        beep( .1,1200 )
                        beep( .08,880 )
                        print "\n***End of Cycle.***"
                        print

            repeat = raw_input( "Press [<y>] or [<enter>] to continue. Press[<n>] to stop: " )
            if repeat == "n":
                outfile.close()
                print
                print "*************************"
                print "***  End of program   ***"
                print "*************************"
                break
            if repeat == " ":
                continue

    except KeyboardInterrupt,SyntaxError:
        outfile.close()
        print "\nLoop canceled."



