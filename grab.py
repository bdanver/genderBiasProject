import os 
import re
from os import listdir
from os.path import isfile, join
from pathlib import Path

path="put your path here"

# Best way to move the new files from terminal:
# mv *-short.txt directoryname/ 

# Attempt to make new directory from .py file 
# path2="path to make a new directory with new files"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# Grabs Link, Summary and Experience 
def getInfo():  
    for file in onlyfiles:
            with open(join(path, file), 'r') as f:
                lines = f.readlines() 
                summaryFound = False
                # experienceFound = False
                if lines[1].startswith('www.linkedin.com/in/') and lines[1].endswith('(LinkedIn)\n'):
                    # os.mkdir(path2, exist_ok=True)
                    outfile = open(join(file[:-4] + "-short.txt"), 'w')
                    outfile = open(file[:-4] + "-short.txt", 'w')
                    outfile.write(lines[1])
                for line in lines:
                    if line == 'Summary\n':
                        summaryFound = True
                    if summaryFound:
                        outfile.write(line)
                        # print(line.rstrip('\n'))

                        # Need to find a way to not read in Education line
                        # Need a peek method
                        if line == 'Education\n':
                            # print('\n')
                            outfile.write('\n')
                            break

                    # If want to separate Experience from Summary 

                    # if line == 'Experience\n':
                    #     experienceFound = True
                    # if experienceFound:
                    #     print(line.rstrip('\n'))
                    #     if line == 'Education\n':
                    #         print('\n')
                    #         break
                        
# Driver Code 
if __name__ == '__main__': 
    getInfo()
  