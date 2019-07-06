import re

inputstr = "BACD102354"
#for _ in range(int(inputstr())):
word = "".join(sorted(inputstr))
print(word)
try:
    assert re.search(r'[A-Z]{2}', word)
    assert re.search(r'[\d]{3}', word)
    assert re.search(r'[A-Za-z0-9]+', word)
    assert not re.search(r'(.)\1', word)
    assert len(word) == 10
except:
    print("Invalid")
else:
    print("Valid")