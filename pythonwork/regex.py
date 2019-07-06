import re

with open("/home/s.verma1/Pythonwork/address", 'r') as reader:
     data = reader.readline()
     print(type(reader))
     newdata = re.split(":? ", data, 4)
     print(newdata, end='')

