import re
import csv


def logprocess(input, output):
    with open(input, 'r') as reader, open(output,'w') as writer:
         csv_out = csv.writer(writer)
         csv_out.writerow(['IP','Time', 'Http Commands', 'Http status'])
         for line in reader:
             try:
                    pattern = r"([\d{1,3}\.]+) - - \[(.*?)\] \"(.*?)\" (\d+) (\d+) \"(.*?)\" \"(.*?)\""
                    match = re.search(pattern, line)
                    list1 =  []
                    for number in 1,2,3,4:
                        list1.append(match.group(number))

                    print(list1)
                    #returnelist = list(match.groups())
                    csv_out.writerow(list1)
             except AttributeError:
                    match = None

if   __name__ == '__main__' :
    logprocess('/home/s.verma1/Pythonwork/apache_logs','/home/s.verma1/Pythonwork/apache_logs_outfile')
