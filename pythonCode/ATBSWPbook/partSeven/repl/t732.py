#! /usr/bin/python3
import re
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a whell')
#print(mo.group(), mo.group(1), mo.group(2))
print(mo.group(), mo.group(1))
