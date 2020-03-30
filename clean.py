import os 
import re
from os import listdir
from os.path import isfile, join

path="put your path here"
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# Check if first line is word 'Contact' 
def checkContact():    
    for file in onlyfiles:
        with open(join(path, file), 'r') as f:
            lines = f.readlines()
            if not lines[0] == 'Contact\n':
                print(file)
                print("First line not Contact:", lines[0])

#Check if second line is LinkedIn link. Consume until reach '(LinkedIn)' 
def checkLink():
    for file in onlyfiles:
        with open(join(path, file), 'r') as f:
            lines = f.readlines()
            if lines[1].startswith('www.linkedin.com/in/') and lines[2].endswith('(LinkedIn)\n'):
                l = []
                l.append(lines[1].rstrip('\n'))
                l.append(lines[2])
                s = ''.join(l).rstrip('\n')
                #print(file)
                #print(s)
                with open(join(path, file), 'w') as f:
                    for i, line in enumerate(lines, 1):
                        if i == 2:
                            f.writelines(s)
                        elif i == 3:
                            f.writelines('\n')
                        else: 
                            f.writelines(line)
            # For now, just seeing which files don't have LinkedIn link on Second Line 
            elif not lines[1].startswith('www.linkedin.com/in/'):
                print(file)
                print("Second line not LinkedIn link:", lines[1])
            
            # Find line with LinkedIn link. Join it with next line '(LinkedIn)'
            # Attempted to swap the contents on the 2nd line with the link
	    # If you run this now will delete this entire file 	
	            
            # elif not lines[1].startswith('www.linkedin.com/in/'):
            #       with open(join(path, file), 'w') as f:
            #         for i, line in enumerate(lines, 1):
            #             lookup = re.match(r'www.linkedin.com/in/(.*)', line)
            #             if lookup:
            #                 l = []
            #                 l.append(line.rstrip('\n'))
            #                 l.append(lines[i])
            #                 fullLink = ''.join(l).rstrip('\n')
            #                 if i == 2:
            #                     f.writelines(fullLink)
            #                 else:
            #                     f.writelines(line)
            #                 print(file)
            #                 print(s)

            # Debug statements 
            # print("Found: ", i, "Line: ",line) #linkedin start
            # print("Next: ", i, "Line next: ", lines[i]) #next line    
            # print(file)
            # print(lines[1])
            # else:
            #     print(file)
            #     print('Else')


# Driver Code 
if __name__ == '__main__': 
    checkContact()
    checkLink()
