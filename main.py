import re

"""a = re.findall(r"\d+", "asdasds123465a,asd123584")
print(a)"""

"""it = re.finditer(r"\d+", "asdasds123465a,asd123584,1a22")
for i in it:
    print(i.group())"""

"""
s = re.search(r"\d+", "asdasds123465a,asd123584,1a22")
print(s)

"""

"""s = re.match(r"\d+", "123465a,asd123584,1a22")
print(s)
"""

obj = re.compile(r"\d+")
asd = obj.finditer("13215,sg,546")
for i in asd:
    print(i.group())





