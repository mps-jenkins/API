import fileinput
inputfiles = ["/home/s.verma1/IdeaProjects/pythonwork/syslogprocess_csvoutput.py", "/home/s.verma1/IdeaProjects/pythonwork/csvreaderandsort.py"]

with open("/home/s.verma1/IdeaProjects/pythonwork/concatenate.out", 'w') as outfile:
    with fileinput.input(files=('/home/s.verma1/IdeaProjects/pythonwork/syslogprocess_csvoutput.py', '/home/s.verma1/IdeaProjects/pythonwork/csvreaderandsort.py')) as f:
        for line in f:
            process(line)

