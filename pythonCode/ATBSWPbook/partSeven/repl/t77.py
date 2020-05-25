#! /usr/bin/python3
import re
vowelRegex1 = re.compile(r'[aeiouAEIOU]')
vowelRegex2 = re.compile(r'[^aeiouAEIOU]')
string = 'llRAFDAFfasdfashfl asjfluioqtyrorwbnzxcvnkhvkasfak'
string1 = vowelRegex1.findall(string)
string2 = vowelRegex2.findall(string)
print(string1, string2)
