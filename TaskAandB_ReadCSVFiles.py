"""Import required Libraries"""
from TaskAandB_Config import *
from TaskAandB_FunctionLibrary import *

"""Call the Read file lines to read the Top30_airports.latlong.csv file"""
airportdataset = Read_Filelines(loc_of_airportfile, 'airport')

"""Call the Read Filelines Function to read the "AComp_passenger_data_no_error.csv" 
file"""
passengerdataset = Read_Filelines(loc_of_passengerfile,'passenger')

"""Call the updateairport name to replace airport code with airport name in passenger list"""
passengerdataupdated = UpdateAirportName(airportdataset,passengerdataset)