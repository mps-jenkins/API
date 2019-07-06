import re

def plural(noun):
    if re.search(r"[sxz]$", noun):
        return re.sub('$','es', noun)
    elif re.search(r"[^aeiou]h$",noun):
        return re.sub('$','es',noun)
    elif re.search('[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'



print(plural("toy"))