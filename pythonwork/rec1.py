#! \usr\bin\python

def main():
    print (recurfunc(10))

def recurfunc(val):
    if val == 1:
        return 1
    else:


        print (val)
        return val + recurfunc(val - 1)


main()