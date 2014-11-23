"""
A table is a list of the format:
table[0] = <list>Traits; List of predefined <str>traits in their predefined positions
table[1] = <int>Lower Bound; The lowest user-input value
table[2] = <int>Upper Bound; The highest user-input value
table[3] = <int>Offset; The difference between 0 and the Lower Bound
(In case the user's lower bound is 7, since python lists start at index 0)
"""

from random import randint
from os import getcwd, listdir
from os import sep as SEP

ASTERISK = "Asterisk"
DIRECTORY = "Tables"
FILES_TO_OPEN = listdir(getcwd()+SEP+DIRECTORY)

def main():
    tables = Open_All_Files()
    print "Press Enter for a new Character."
    while True:
        raw_input() # Requires user to Press Enter
        print Roll_All_Tables(dict(tables))

def Open_All_Files():
    """
    Opens every file and extracts its data
    Returns this data as 'tables' to be 'rolled' on
    """
    tables = {}

    # For all files that don't start with '~'
    for filename in FILES_TO_OPEN:
        if filename[0] != '~':
            
            # Get the data, split into lines
            with open(DIRECTORY+SEP+filename,'r') as f:
                lines = f.read().split('\n')

            # If the content is the name of a text file, add a flag instead
            if lines[0] in FILES_TO_OPEN:
                tables[filename[:-4]] = lines[0][:-4]

            # Otherwise
            else:
                # Split each line into Num,Text
                data = [line.split('. ') for line in lines]

                # Assign Bounds
                # Lower Bound not a range
                if '-' not in data[0][0]:
                    low = int(data[0][0])

                # Lower Bound a range
                else:
                    thing1, thing2 = data[0][0].split('-')
                    low = int(thing1)
                    
                # Upper Bound not a range
                if '-' not in data[-1][0]:
                    upp = int(data[-1][0])
                    
                # Lower Bound a range
                else:
                    thing1, thing2 = data[-1][0].split('-')
                    upp = int(thing2)
                
                off = 0 - low           # lists start at 0
                lst = Extract_Cautiously(data, upp, off)
                tables[filename[:-4]] = (lst, low, upp, off)

    # Catch Flags
    for key in tables:
        if type(tables[key]) is str:
            tables[key] = tables[ tables[key] ]

    return tables

def Extract_Cautiously(data, upp, off):
    # Prep the list with empty values
    lst = ['ERROR' for x in xrange(upp)]
    for line in data:
        
        # If the line is just one number
        if '-' not in line[0]:
            index = int(line[0]) + off
            lst[index] = line[1]
            
        # If the line consists of a range of numbers
        else:               
            index1, index2 = line[0].split('-')
            index1 = int(index1) + off
            index2 = int(index2) + off
            lst[index1:index2] = [line[1]]*(index2-index1)

    return lst

def Roll_All_Tables(tables):
    Result = {}
    
    # For Speech, Hair and Face
    for traitName in tables:
        Result[traitName] = "\t"+Roll_Table(tables[traitName])

    # Get the longest traitname
    LENGTH = 0
    for traitName in tables:
        if len(traitName) > LENGTH:
            LENGTH = len(traitName)
    LENGTH += 2

    # Construct our message
    msg = ''
    for traitName in Result:
        tab = ":" + (' '*(LENGTH - len(traitName)))
        msg += '\n' + traitName + tab + Result[traitName]
        
        # Check for Asterisks
        if Result[traitName][-1] == "*":
            msg += " ("+Roll_Table(tables[ASTERISK])+")"
        
    return msg

def Roll_Table(table):
    result = "ERROR"
    while result == "ERROR":
        diceRoll = randint(table[1],table[2])
        diceRoll += table[3]
        result = table[0][ diceRoll ]
    return result

def Try_Open_All_Files():
    """
    In case Open_All_Files() raises an exception,
    this can be seen from the command line.
    """
    try:
        tables = Try_Open_All_Files()
    except:
        print "ERROR: COULD NOT OPEN FILES"
        raw_input() # Requires user to Press Enter
        raise
    return tables

def Try_Roll_All_Tables(tables):
    """
    In case Roll_All_Tables() raises an exception,
    this can be seen from the command line.
    """
    try:
        result = Try_Roll_All_Tables(tables)
    except:
        print "ERROR:\tCOULD NOT ROLL DICE"
        raw_input() # Requires user to Press Enter
        raise
    return result
    
if __name__ == "__main__":
    main()
