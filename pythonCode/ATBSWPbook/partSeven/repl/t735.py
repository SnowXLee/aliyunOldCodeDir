#! /usr/bin/python3
import re
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')
mo2 = batRegex.search('The adventures of Batwowowoman')
mo3 = batRegex.search('The adventures of Batman')
print(mo1.group(), mo2.group(), mo3)
