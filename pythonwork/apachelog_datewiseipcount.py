from collections import Counter
import re

dict1  = {}
dict2 = {}

def pretty(dict2, indent=0):
    for key, value in dict2.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))




with open("/home/s.verma1/Pythonwork/test.log",'r') as input:
    for line in input:
        match1 =  re.match(r'(?P<IP>[\d{3}.]+).*\[(?P<time>.*)\]\s"(?P<request>.*?)"\s(?P<code>\d+)',line)
        ip = match1.group('IP')
        date = re.split(':',match1.group('time'))[0]
        time = re.split(': +',match1.group('time'),3)[0]
        request = match1.group('request')
        code = match1.group('code')
        dict1.setdefault(date,[]).append(ip)
        for key, value in dict1.items():
            dict2[key] = dict((i, value.count(i)) for i in value)
        pretty(dict2)

