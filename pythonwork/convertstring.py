def to_string(n,base):
    convertstring = "0123456789ABCDEF"
    if  n < base:
        return convertstring[n]
    else:
        return to_string(n//base,base) + convertstring[n%base]


print(to_string(90,10))