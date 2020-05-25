#! /usr/bin/python3
import re
beginsWithHello = re.compile(r'Hello')
str1 = beginsWithHello.search('Hello world!').group()
endsWithNumber = re.compile(r'\d$')
str2 = endsWithNumber.search('Your number is 42.')
str3 = endsWithNumber.search('Your number is forty two.')
wholeStringIsNum = re.compile(r'^\d+$')
str4 = wholeStringIsNum.search('13412341').group()
str5 = wholeStringIsNum.search('134sdfio1342134')
print(str1, str2, str3, str4, str5)
