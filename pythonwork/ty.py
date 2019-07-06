def print_reverse(string_list):
    dict = {}
    for str in string_list:
        print(str)
        if dict[str]:
            print(str)
            print(''.join(reversed(str)))
            dict[''.join(reversed(str))] = 1


list="youarewthene"
print_reverse(list)