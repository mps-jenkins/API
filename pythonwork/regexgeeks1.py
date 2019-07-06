import re

input="ankitrai326"

match= re.search('[0-9]+$', input)
print(match.group())


