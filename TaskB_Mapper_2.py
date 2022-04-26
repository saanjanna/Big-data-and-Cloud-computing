import sys
from TaskAandB_Config import *

"""function is defined to map the passenger_ID and flight_ID keys"""

"""TaskB_Mapper_2 Define mapper function to map the flight and airport name keys"""
def TaskB_Mapper_2():
    """Iterate each line of input line"""
    for line in sys.stdin:
        """Split the line by comma"""
        singleline = line.strip().split(',')
        """Verify if line is empty"""
        if len(singleline) > 1:
            """Remove all the special charaters of 1st Elemnent of passenger_ID in the line"""
            singleline[0]=''.join (e for e in singleline[0] if e.isalnum())
            """Remove all the special charaters of 2nd Elemnent of flight_ID in the line"""
            singleline[1]=''.join (e for e in singleline[1] if e.isalnum())
            """Combine passenger_id and flight_ID"""
            passengerflight = singleline[0],"_",singleline[1]
            """Map each passenger flight key to 1 and print"""
            print('%s\t%s'%(passengerflight,1))
            """Append the flight airport list to store all the list created in flight airport"""
            passengerflightlist.append(passengerflight)
            """Return passenger flight list"""
            return passengerflightlist

"""Call Task b mapper 2 definition"""
TaskB_Mapper_2()