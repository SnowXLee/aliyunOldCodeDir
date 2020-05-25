#! /usr/bin/python3
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(), mo.group(), mo.group(1), mo.group(2), mo.groups()) 
mo2 = phoneNumRegex2.search('My number is (415) 555-4242.')
print(mo2.group(1))
