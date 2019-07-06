#! /usr/bin/python
import re
import csv

newdict = {}
dict1 = {}
with open("/home/s.verma1/Pythonwork/apache_logs",'r') as inputfile, open("new.csv",'w') as writer1:
    for line in inputfile.readlines():
        pattern = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
        ipaddress = re.search(pattern, line).group()
        if ipaddress in dict1:
            dict1[ipaddress] += 1
        else:
            dict1[ipaddress] = 1
        pattern1= r"([\d\.]+).*\[(.*)\]\s\"(.*?)\""
        match = re.search(pattern1, line)
        #print(match.groups())
        out = csv.writer(writer1)
        out.writerow(match.groups())
        list1 = [match.group(1), match.group(3)]
        time = match.group(2)
        newdict.setdefault(time,[]).append(list1)
    print(newdict.items()
          )





