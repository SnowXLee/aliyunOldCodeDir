#! /usr/bin/python3
import re
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: AL Last Name: Sweigart').group()
nongreedyRegex = re.compile(r'<.*?>')
mo1 = nongreedyRegex.search('<To serve man> for dinner.>').group()
greedyRegex = re.compile(r'<.*>')
mo2 = greedyRegex.search('<To Serve man> for dinner.>').group()
print(mo, mo1, mo2)
