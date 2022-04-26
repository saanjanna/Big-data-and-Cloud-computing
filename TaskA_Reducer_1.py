import sys
import re
from TaskAandB_Config import *

def TaskA_Reducer_1():
    """Task A Reducer 1 function is defined to get the total number of flights"""
    """prev_count, prev_code"""
prev_code = None
prev_airportcode = None
prev_count = 0
newcode = None
count = 0

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
        count = int(newcount)
    except ValueError:
        print("Oops!  That was not an integer.  Try again...")
        continue
"""Compare if newcode read from the input line is equal to the previous code"""
if prev_code == newcode:
    """if both the codes are same then increment the previous count with count"""
    prev_count += count
else:
    prev_code = newcode
    prev_code1 = prev_code.strip().split('_',1)
    airport_name, flight_code = prev_code1
    falist = airport_name, flight_code, prev_count
    """Create a new list to store all the lists formed above"""
    flightairportreduced.append(falist)

"""Iterate to each list of flight airport reduced to get total number
of flights from each airport"""
for eachlist in flightairportreduced:
    """Assign Count to 0"""
    count =0
    """Assign each element of eachlist to seperate variable"""
    airport_name, flight_code, prev_count = eachlist
    """Verify if the airportcode is different from prev_airportcode"""
    if prev_airportcode is airport_name:
        """Iterate each list of flightairportreduced to count the total 
        number of flights"""
        for each in flightairportreduced:
            """Assign each element of each to seperate variable"""
            airport_name1, flight_code, prev_count = each
            """Verify if the airport names match then increment the count by 1
            and replace prev_airportcode"""
            if airport_name==airport_name1:
                count +=1
                prev_airportcode = airport_name
            else:
                continue
        print('%s - Total number of flights = %s' % (airport_name,count))

"""Call reducer_level1"""
TaskA_Reducer_1()