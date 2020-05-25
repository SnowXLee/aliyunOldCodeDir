#! /usr/bin/python3
import re
robocop = re.compile(r'robocop', re.IGNORECASE)
str1 = robocop.search('RoboCop is part man, part machine, all cop.').group()
str2 = robocop.search('ROBOcOp protects the innocent.').group()
str3 = robocop.search('AI, why does your programming book talk about\
                       robocop so much?').group()
print(str1)
print(str2)
print(str3)
