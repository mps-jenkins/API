from itertools import groupby

def remove_dups(string):
    unique = (i[0] for i in groupby(string))
    return ''.join(unique)


print(remove_dups("Shreeeettttiiiii veraammaa"))