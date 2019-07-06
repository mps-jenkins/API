import re

dict_data = {}
logfile = '/home/s.verma1/Pythonwork/syslog'

with open(logfile, 'r') as reader:
    for line in reader:
        print(line)
        protocol = re.search(r"(\D)\[.*\]", line)
        print(protocol.groups())
        #protocol = line.split(" ")[4]  | re.search(r"(\D)\[")
        print(protocol)
        #protocolkey = re.search(r"(\D)\[", protocol)
        timesamp = line.split(" ")[2]
        dict_data[protocolkey] = timesamp

for (key, value) in dict_data.items():
    print(key , " :: ", value)


