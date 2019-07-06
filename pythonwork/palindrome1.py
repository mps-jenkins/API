

def ispalind(string):
    m = len(string) / 2
    for i in range(m):
        j = i + 1
        if string[i] == string[-j]:
            return True
    return False

print(ispalind("Shreeti"))