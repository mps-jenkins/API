def print_json(data):
    if type(data) == dict:
        for k, v in data.items():
            print k
            print_json(v)
    else:
        print data

        def pretty(d, indent=0):
    for key, value in d.iteritems():
        if isinstance(value, dict):
            print '\t' * indent + (("%30s: {\n") % str(key).upper())
            pretty(value, indent+1)
            print '\t' * indent + ' ' * 32 + ('} # end of %s #\n' % str(key).upper())
        elif isinstance(value, list):
            for val in value:
                print '\t' * indent + (("%30s: [\n") % str(key).upper())
                pretty(val, indent+1)
                print '\t' * indent + ' ' * 32 + ('] # end of %s #\n' % str(key).upper())
        else:
            print '\t' * indent + (("%30s: %s") % (str(key).upper(),str(value)))

            def pretty(d, indent=0):
    if isinstance(d, dict):
        for key, value in d.iteritems():
            print '\t' * indent + str(key)
            if isinstance(value, dict) or isinstance(value, list):
                pretty(value, indent+1)
            else:
                print '\t' * (indent+1) + str(value)
    elif isinstance(d, list):
        for item in d:
            if isinstance(item, dict) or isinstance(item, list):
                pretty(item, indent+1)
            else:
                print '\t' * (indent+1) + str(item)
    else:
        pass