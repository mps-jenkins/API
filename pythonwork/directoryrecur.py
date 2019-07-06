import os

def processdir(mydir):
    dirname = os.path.abspath(mydir)
    print(dirname)
    files = os.listdir(mydir)
    for filename in files:
        filepath = os.path.join(dirname,filename)
        if os.path.isfile(filepath ):
            #print(filepath)
            print("")
        elif os.path.isdir(filepath):
            processdir(filepath)

processdir("/home/s.verma1/Documents")
#print(processdir("/home/s.verma1/Documents"))