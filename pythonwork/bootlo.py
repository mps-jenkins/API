import re

with open("/home/s.verma1/Pythonwork/boot.log",'r') as inputfile:
    for line in inputfile:
        #print(line)
        pattern = r"\[.*OK.*\]\s(.*)"
        match = re.search(pattern,line)
        if match:
            print(match.group(1))
