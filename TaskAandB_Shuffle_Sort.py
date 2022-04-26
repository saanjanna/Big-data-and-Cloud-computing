import sys
from TaskAandB_Config import *

"""Shuffle sort method is defined to sort the input of key and value getting from mapper"""

def TaskAandB_Shuffle_Sort():
    """Iterate all inputs coming from mapper"""
    for lines in sys.stdin:
        """Split the line by tab"""
        lines = lines.strip().split('\t', 1)
        """Input line is split into key and values"""
        code, count = lines
        """key are taken into a list"""
        sortlist.append(code)
        
        """Sort Key"""
        sortlist.sort()
        """Iterate over the list of keys and print the key and Value pair"""
        for each in sortlist:
            print('%s\t%s' % (each,1))

"""Call Shuffle_Sort method to sort the key and value"""
TaskAandB_Shuffle_Sort()