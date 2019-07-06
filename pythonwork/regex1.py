import re

str= "..123456789101112131415161718202144445"
m = re.search(r'([A-Za-z0-9])\1+', str)
print(m.group(1) if m else -1)


str2="100,000,000.000"
match = re.split(r'[,.]+',str2)
print(match)

st = [1,2,3,4,5]
list1 = [ x**2 for x in st]
print(list1)