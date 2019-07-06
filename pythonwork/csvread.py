import csv

csvfile = '/home/s.verma1/Pythonwork/csv1.csv'
csvfile2 = '/home/s.verma1/Pythonwork/csv2.csv'

dict1 = {}
matched = []


with open(csvfile, newline='') as csv1, open(csvfile2, newline='') as csv2:
    csvreader = csv.DictReader(csv1, delimiter=',')
    csvreader1 = csv.DictReader(csv2, delimiter=',')
    for row in csvreader:
        for row1 in csvreader1:
            dict1.append(row1)
        for k, v in dict1:
            print(k, v)




