import re

pattern = re.compile(r"\(?(\d{3})\)?[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})\D*(\d+)")
#pattern = re.compile(r"\(?(\d{3})\)?\D*(\d{3})\D*(\d{4})")

print(pattern.search("415-867-5309 ext. 9999").groups())