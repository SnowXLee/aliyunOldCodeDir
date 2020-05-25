#! /usr/bin/python3
import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo1.group(), mo2.group())
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phoneRegex.search('My number is 415-555-4242')
mo4 = phoneRegex.search('My number is 555-4242')
print(mo3.group(), mo4.group())
