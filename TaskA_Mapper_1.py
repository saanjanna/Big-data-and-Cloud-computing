import sys
from TaskAandB_Config import *

"""Define mapper function to map the flightID and airport name keys"""
def TaskA_Mapper_1():
    """Iterate each line of input line"""
    for line in sys.stdin:
        """Split the line by comma"""
        singleline = line.strip().split(',')
        """Verify if line is empty"""
        if len(singleline) > 1:
            """Remove all the special charaters of 3rd Elemnent of airport name in the line"""
            singleline[2]=''.join (e for e in singleline[2] if e.isalnum())
            """Remove all the special charaters of 2nd Elemnent of airport name in the line"""
            singleline[1]=''.join (e for e in singleline[1] if e.isalnum())
            """Combine flight_id with airport_name"""
            flightairport = singleline [2] + '_' + singleline [1]
            """Map each flight airport key to 1 and print it"""
            print('%s\t%s'%(flightairport,1))
            """Append the flight airport list to store all the list created in flight airport"""
            flightairportlist.append(flightairport)
            """Return flight airport list"""
            return flightairportlist

"""Call mapper level"""
TaskA_Mapper_1()