import re

with open('/home/s.verma1/Pythonwork/file','r') as inputd, open('/home/s.verma1/Pythonwork/out','w') as outd:
    for lines in inputd:
        linenew = re.sub("\d+\.+", "\n\r", lines)
        print(linenew)
