import re


string = "Shreeti verma: 8998-7870-11 241 Smithwood St"
#list1 = re.split(':? ',string, 4)
#print(list1)

m = re.match(r"(?P<firstname>\w+) (?P<lastname>\w+)", string)
print(m.groupdict())