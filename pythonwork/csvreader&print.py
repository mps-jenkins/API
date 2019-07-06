import csv

fields = []
rows = []
filename = '/home/s.verma1/Pythonwork/csv1.csv'
with open(filename, 'r') as csvfile1:
    csv_reader = csv.reader(csvfile1, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are:' + ", ".join(row))
            line_count += 1
        else:
            #print("'{}' works in the '{}' department, and was born in".format(row[1], row[2]))
            line_count += 1
    print("Processed '{}' lines".format(line_count))