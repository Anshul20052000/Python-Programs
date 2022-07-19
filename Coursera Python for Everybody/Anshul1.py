import re
hand = open('Actual File.txt')
numlist = list()
for line in hand:
    line =line.rstrip()
    stuff=re.findall('[0-9]+',line)
    for a in stuff:
        num=float(a)
        numlist.append(num)
print(sum(numlist))
