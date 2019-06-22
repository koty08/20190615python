import re

p= re.compile('[a-z]+')

m = p.finditer("PytH0n")
print(m)

for i in m:
    print(i)