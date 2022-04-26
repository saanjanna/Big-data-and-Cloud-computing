"""Variable to store location of Top30 airports lat and long csv data file"""
loc_of_airportfile = "C:/Users/HP/Desktop/sanju/Cloud Computing/Top30_airports_LatLong.csv"
"""Variable to store location of passenger csv data file"""
loc_of_passengerfile = "C:/Users/HP/Desktop/sanju/Cloud Computing/AComp_Passenger_data_no_error.csv"

"""Variable for reducer function"""
"""prev_count=0
prev_count=1"""

"""datasetairport variable is defined to store the list of airport dataset"""
datasetairport = []

"""dataset passenger variable is defined to store the list of passenger dataset"""
datasetpassenger = []

"""datasetupdated passenger variable is defined to store teh list of updated passenger dataset"""
datasetupdatedpassenger = []

"""Flight airport list Variable is defined to store the list of mapper1.py mapper output"""
flightairportlist = []

"""Flight airport reduced variable is defined to store the result list in new reducer function"""
flightairportreduced = []

"""Passenger flight list variable is defined to store the list of mapper level 1.py mapper out"""
passengerflightlist = []

"""Passenger flight reduced variable is defined to store the result list in reducer2 function"""
passengerflightreduced =[]

"""Passengerflighttotal variable is defined to store the total number of flights of all passenger"""
passengerflighttotal =[]

"""Sortlist Variable defined to store the sorted list"""
sortlist = []