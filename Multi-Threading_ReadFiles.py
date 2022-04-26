"""Importing required libraries"""
import threading
from threading import *
from time import sleep
from TaskAandB_Config import *
from TaskAandB_FunctionLibrary import *

"""Calling functions to setup data"""
if __name__ == "__main__":
    """Create thread object to read the Top30_airports.latlong.csv file"""
    thread1 = threading.Thread (name='Read_Filelines', target = Read_Filelines, args=(loc_of_airportfile, 'airport'))
    
    """Create thread object to read the AComp_passenger_data_no_error.csv file"""
    thread2 = threading.Thread (name='Read_Filelines', target = Read_Filelines, args=(loc_of_passengerfile,'passenger'))
    
    """Start the Thread"""
    thread1.start()
    sleep(1)
    thread2.start()
    sleep(1)
    
    """Join the thread"""
    thread1.join()
    thread2.join()
    
    """Verify above threads are running"""
    if thread1.is_alive() or thread2.is_alive():
        sleep(0.1)
    else:
        """if the thraeds have stopped, then initiate a new thread to udpate the airportname in passenger list 2"""
        thread3 = threading.Thread(name='Update_AirportName',target=Update_AirportName, args=(datasetairport,datasetpassenger))
        """Start the thread"""
        thread3.start()
        """Join the thread"""
        thread3.join()