def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        print(toStr(n//base,base))
        print(convertString[n%base])
        return toStr(n//base,base) + convertString[n%base]

print(toStr(33,4))
