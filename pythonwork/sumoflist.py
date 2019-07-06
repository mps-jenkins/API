#! /usr/bin/python

list1 = (1, 2, 10, 34, 22)


def addlist(listing):
    if len(listing) == 1:
        return listing[0]
    else:
        return listing[0] + addlist(listing[1:])


print(addlist(list1))
