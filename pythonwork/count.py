li1 = ['77.0.42.68', '207.241.237.101', '120.202.255.147', '207.241.237.104', '207.241.237.225', '207.241.237.101', '50.16.19.13', '100.43.83.137', '46.105.14.53', '66.249.73.135', '207.241.237.227', '79.235.40.176', '79.235.40.176']

#for i in li1:
newdict = dict((i, li1.count(i)) for i in li1)
print(type(newdict))