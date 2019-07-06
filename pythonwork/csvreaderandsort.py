import csv

fields = []
rows = []
filename = '/home/s.verma1/Pythonwork/csv1.csv'
with open(filename, 'r') as csvfile1:
       csvreader = csv.reader(csvfile1)
       fields = next(csvreader)
       print(fields)
       for row in csvreader:
           rows.append(row)
       print(rows)
       print("no of rows: '{}'" .format(csvreader.line_num))

       print("Nname of fields " + ', '.join(field for field in fields))

for row in rows[:2]:
     for col in row:
          print("%5s"%col),
     print('\n')