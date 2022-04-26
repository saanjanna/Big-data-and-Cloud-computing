from TaskAandB_Config import*
"""import pandas as pd"""

"""Function Declaration"""
"""Read all the lines in the CSV file"""
def Read_Filelines(Loc_of_file,file_keywords):
    """Open the CSV file from its location and store in the file varibale"""
    file = open(Loc_of_file, 'r')
    
    """Read all the lines from the CSV file and store it in Contenttofile variable"""
    Content_of_file = file.readlines()
    
    """Iterate each line in the Content to file variable and form a dict. object variable"""
    """datasetairport.clear()
    datasetpassenger.clear()"""
    
    for each_line in Content_of_file:
        """Split each line with ',' and store it in line Variable"""
        line=each_line.strip().split(',')
        """Verify if line is empty"""
        if len(line)>1:
            """Call the Convert_Lines Dict function that creates a 
            dictonary(key,value) type variable for each line"""
            dataset = Convert_LinesDict(line,file_keywords)
    """Close the File"""
    file.close()
    """Return the dataset established"""
    return dataset

"""Function to covert the list of lists into dictnorary object and 
store the dataset in a dict object form"""
def Convert_LinesDict(line, file_keyword):
    """Check if the file key word is 'airport' and then create a list of its elements"""
    if file_keyword == 'airport':
        """Assign each element of line to seperate variable"""
        airport_name, airport_code, lat, long = line
        """from a list with airport_name and airport_code"""
        listoflines_airport = airport_name, airport_code
        datasetairport.append(listoflines_airport)
        return datasetairport
    """Check if the file keyword is 'passenger' and then create list of its elements"""
    if file_keyword == 'passenger':
        """Assign each element of line to seperate variable"""
        pasngr_id, flight_id, from_airport, dest_airport, dep_time, flight_time = line
        """form a list with passenger details"""
        listoflines_pasngr = pasngr_id,flight_id,from_airport
        datasetpassenger.append(listoflines_pasngr)
        return datasetpassenger

"""Function to update the airport_code and airport_name in passenger dataset"""
def UpdateAirportName(airportdataset, passengerdataset):
    """Iterate each line of the passenger dataset to compare and update the
        airport_code and airport_name"""
    for i, pdata in enumerate(passengerdataset):
        """Assign each element of line to separate variable"""
        pasngr_id, flight_id, from_airport = pdata
        """Verify if line is not empty"""
        if len (airportdataset) > 0:
            """Iterate each line of the passengerdataset to compare and
            update the airport_code and airport_name"""
            for j,adata in enumerate(airportdataset):
                """Assign each elemenet of line to seperate variable"""
                airport_name, airport_code = adata
                """Verify if from_airport from passenger dataset is equal to
                airport_code of airport dataset"""
                if airport_code == from_airport:
                    """Update the list of passenger to have airport_name"""
                    updatedlistofpasngr=pasngr_id, flight_id, airport_name
                    """Print updated list of Passenger"""
                    print(updatedlistofpasngr)
                    """Append the updated list of pasangr into datasetupdatedpassenger 
                    to store all thet list together"""
                    datasetupdatedpassenger.append(updatedlistofpasngr)
                    break