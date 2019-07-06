from collections import Counter

list1= set([12, 34, 56, 67.98])
list2= set([90,78,12,23,11,34])
list3= set([89,12,34,554])

def common(arr1,arr2,arr3):
    arr1 = Counter(arr1)
    arr2 = Counter(arr2)
    arr3 = Counter(arr3)
    common = []
    resultDict = dict(arr1.items() & arr2.items() & arr3.items())
    for key,value in resultDict.items():
        #for i in range(0,value):
            common.append(key)

    print(common)

common(list1,list2, list3)