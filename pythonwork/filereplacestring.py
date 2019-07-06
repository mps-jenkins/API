import fileinput

with fileinput.FileInput("/home/s.verma1/Pythonwork/log", inplace=True, backup=".bak") as input:
    for line in input:
        print(line.replace('ntpd','not ntpd'), end='')