#! /usr/bin/python3
import re
noNewlineRegex = re.compile('.*')
newLineRegex = re.compile('.*', re.DOTALL)
newLineStr = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
str1 = noNewlineRegex.search(newLineStr).group()
str2 = newLineRegex.search(newLineStr).group()
print(str1)
print(str2)
