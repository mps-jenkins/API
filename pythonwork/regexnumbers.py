import re


pattern=r"^9[0-9][0-9]?$|^[1-9]\d{1,2}$"


def matchi(string):
    if re.match(pattern, string):
        print("MATCH")
    else:
        print("NO MATCH")


matchi("1234")