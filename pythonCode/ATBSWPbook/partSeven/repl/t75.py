#! /usr/bin/python3
import re
phoneNumRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
string1 = 'Cell: 415-555-9999 Work: 212-555-0000'
string2 = 'Cell: 415-555-9999 Work: 212-555-0000'
mo1 = phoneNumRegex1.search(string1).group()
mo2 = phoneNumRegex1.findall(string1)
mo3 = phoneNumRegex2.findall(string2)
print(mo1, mo2, mo3)
