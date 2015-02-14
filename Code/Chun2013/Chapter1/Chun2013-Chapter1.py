import re
import keyword

r1 = '[bh]+[aiu]+t'
print(re.findall(r1, "hut"))

r2 = "\w+\s\w+"
print(re.findall(r2, "Tirthankar Chakravarty"))

r3 = "\w+,\s\w"
print(re.findall(r3, 'Chakravarty, T'))

# whether Python identifier
r4 = ('|').join(keyword.kwlist)
print(re.findall(r4, "del"))

# match street addresses
r5 = ''