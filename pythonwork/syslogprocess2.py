import re
import csv

def readfile(inputfile, outfile):
    dict1 = {}
    regex = r"(\w+ \d+ \d+:\d+:\d+)"
    with  open(inputfile, 'r') as input, open(outfile, 'w') as write:
        csv_out = csv.writer(write)
        csv_out.writerow(['date','#count'])
        log = input.read()
        mydatetime =  re.findall(regex, log)
        for date in mydatetime:
            if date in dict1:
               dict1[date] += 1
            else:
               dict1[date] = 1

            for k,v in sorted(dict1.items()):
                outs = [k, v]
                csv_out.writerow(outs)



if __name__ == '__main__':
    readfile("/home/s.verma1/Pythonwork/syslog","/home/s.verma1/Pythonwork/syslogout")

