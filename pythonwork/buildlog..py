import re
from datetime import time

dict1 = {}


def timediff(start, end):
    fmt = '%H:%M:%S'
    tdiff = time.strptime(end, fmt) - time.strptime(start, fmt)
    print("time diff"  + tdiff)


with open("/home/s.verma1/Pythonwork/build.log",'r') as input:
    for line in input:
        data =  re.split("\s", line, maxsplit=3)
        ip = data[0]
        datetime = data[1]
        info = data[3]
        if re.search(r".*Start", info):
            buildnumber =  re.search(r"Build\s#(\d)\b.*", info).groups(1)
            print(datetime)
            starttime = re.search(r".*(?P<time>(\d{2}:){2}\d{2})",datetime).group(1)
            print(starttime)
            dict1[buildnumber] = {}

            dict1.setdefault(buildnumber,{}).setdefault("start", starttime)
        elif re.search(r".*End", info):
            buildnumber =  re.search(r"Build\s#(\d)\b.*", info).groups(1)
            print(datetime)
            endtime = re.search(r".*(?P<time>(\d{2}:){2}\d{2})",datetime).group(1)
            print(endtime)
            dict1[buildnumber]["end"] = endtime

for k,v in dict1.items():
    start1 = v["start"]
    end1 = v["end"]
    timediff(start1, end1)

