import sys
import re
from TaskAandB_Config import *

def TaskB_Reducer_2():
    """Task A Reducer 1 function is defined to get the total number of flights"""
    """prev_count, prev_code"""
prev_pscode= None
prev_pscount=0
newcode = None
count=0

"""Iterate each line of the line received from TaskAandB_Shuffle_Sort.py"""
for line in sys.stdin:
    """Split the line"""
    line = line.strip().split('\t', 1)
    """Assign each element of line to seperate variable"""
    code, count = line
    """Remove the special character from the code"""
    code1 = re.sub("[()]", "", code)
    """Remove the special character from the code1"""
    newcode = re.sub("'", "", code1)
    """Remove the special character from the count"""
    newcount = re.sub("[()]", "", count)
    """Convert string count into int"""
    try:
        count = int(maxcount)
    except ValueError:
        print("Oops!  That was not an integer.  Try again...")
        continue
"""Compare if newcode read from the input line is equal to the previous code"""
if prev_pscode == newcode:
    """if both the codes are same then increment the previous count with count"""
    prev_pscount += count
else:
    prev_pscode = newcode
    prev_pscode1 = prev_pscode.strip().split('_',1)
    passenger_code, flight_code = prev_pscount
    pflist = passenger_code, flight_code, prev_pscount
    """Create a new list to store all the lists formed above"""
    passengerflightreduced.append(pflist)

"""Iterate to each list of flight airport reduced to get total number
of flights from each airport"""
for eachlist in passengerflightreduced:
    """Assign Count to 0"""
    count =0
    """Assign each element of eachlist to seperate variable"""
    passenger_code, flight_code = prev_pscount = eachlist
    """Verify if the passenger code is different from prev_pscode"""
    if prev_pscode == passenger_code:
        """Iterate each list of passengerflightreduced to count the total 
        number of flights"""
        for each in passengerflightreduced:
            """Assign each element of each to seperate variable"""
            passenger_code1, flight_code, prev_pscount = each
            """Verify if the airport names match then increment the count by 1
            and replace prev_airportcode"""
            if passenger_code==passenger_code1:
                count +=1
                prev_pscode = passenger_code
            else:
                continue
            pflist = passenger_code, count
            passengerflighttotal.append(pflist)
            maxflightpasngr = {}
            for each in passengerflighttotal:
                maxflightpasngr.setdefault(each(1),(1)).append (each)
                max_flights=max(maxflightpasngr)
                print(maxflightpasngr(max_flights))

"""Call Task b reducer 2"""
TaskB_Reducer_2()