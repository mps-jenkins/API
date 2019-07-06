from collections import Counter
import re
import json
import csv

dict1  = {}
dict2 = {}
count = 0
l = []


def printy(dict3, indent =1 ):
    if type(dict3) == dict:
        for k,v in dict3.items():
            print(" "*indent,k)
            printy(v, indent=3)
    else:
        print(dict3)


with open("/home/s.verma1/Pythonwork/test.log",'r') as input:
    for line in input:
        match1 =  re.match(r'(?P<IP>[\d{3}.]+).*\[(?P<time>.*)\]\s"(?P<request>.*?)"\s(?P<code>\d+)',line)
        ip = match1.group('IP')
        date = re.split(':',match1.group('time'))[0]
        time = re.split(': +',match1.group('time'),3)[0]
        request = match1.group('request')
        code = match1.group('code')
        dict1[date] = {}
        dict1[date][ip] = {}
        for key1 in dict1:
            for key in dict1[date]:
                if re.match(r"GET.*",request):
                    dict2.setdefault(key1,{}).setdefault(key,[]).append(request)

with open('outfile', 'w') as writer:
    for key in dict2:
        for key1 in dict2[key]:
            count = len(dict2[key][key1])
            csvwrite = csv.writer(writer)
            csvwrite.writerow([key, key1, count])
            printy(dict2)











