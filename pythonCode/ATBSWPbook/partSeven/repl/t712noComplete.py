#! /usr/bin/python3
import re
namesRegex = re.compile(r'Agent \w+')
str1 = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to\
                       Agent Bob.')

