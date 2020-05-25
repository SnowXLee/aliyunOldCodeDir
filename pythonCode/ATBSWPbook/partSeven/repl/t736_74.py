#! /usr/bin/python3
import re
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('Ha')
greedyHaRegex = re.compile(r'(He){3,5}')
mo3 = greedyHaRegex.search('HeHeHeHeHe')
greedyHaRegex2 = re.compile(r'(He){3,5}?')
mo4 = greedyHaRegex2.search('HeHeHeHeHe')
print(mo1.group(), mo2, mo3.group(), mo4.group())
