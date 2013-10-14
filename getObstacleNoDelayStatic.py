# Nicolas Perez
# This program takes <loop arg> readings from each distance.

from myro import*
import string
import time

def loop(loop):
    filelocation = raw_input("Input file location(T:\Research\ResearchMay2011\data\textdata\): "  )
    ftype = raw_input("Input attribute (r, w, a) :  ")
    outfile = open(filelocation,ftype)
    cycle = 0
    Count = 0
    try:
                 
         initialtime = time.time()
         p1= input("Enter starting distance: ")
         p2 = input ("Enter the constant displacement distance: ")
         cycle = cycle + 1
         
         raw_input("Press enter to start new cycle <enter>")
         print "Cycle".rjust(50), cycle
         while p1 >= 2:
                    print "Distance: ", p1
                    outfile.write("%d " %p1)
                    for i in range(loop):        
                        x = getObstacle("center")
                        outfile.write("%d, " %x)
                        #wait(0.1)
                        
                    outfile.write("\n")
                    beep(.08,880)
                    beep(.1,1200)
                    raw_input("Move the robot manually then press enter to continue <enter>")
                    p1 = p1 - p2
         print "\n"         
         outfile.write("\n")
         elapsed = (time.time() - initialtime)
         
         outfile.write("%d " %elapsed) 
             
    except KeyboardInterrupt,SyntaxError:
        outfile.close()
        print "\nLoop canceled"
    print "End of cycle".rjust(50)
    outfile.close()
