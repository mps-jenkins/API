import re

dict =  {}
list1 =  []


def counting(text):
    count = 0
    for letter in text:
        #print(letter)
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    list1 = list(dict.keys())
    list1.sort()
    #print(list1)
    for letter in list1:
        if not re.search("\s", letter):
            print(letter, dict[letter])



print(counting('hiS is String with Upper and lower case Letters'))