import re
import csv

dict = {}

inputfile = open("/home/s.verma1/Pythonwork/syslog", 'r')


with open("/home/s.verma1/Pythonwork/syslogout", 'w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['time', 'process', 'processdetails'])
    for line in inputfile:
        try:
            #pattern = re.compile(r"(?P<Time>\w+ \d+ \d+:\d+:\d+).*\b(?P<process>\w+\-?\w+)\[.*\](?P<processdet>\w+)")
            pattern = re.compile(r"(\w+ \d+ \d+:\d+:\d+).*\b(\w+\-?\w+)\[.*\]")
            data = pattern.search(line)
            result = data.groups()
            print(result)
            csv_out.writerow(result)
        except AttributeError:
            pattern = None


for k,v in dict.items():
    print(k,v)
