import os
searchPath = '/opt/code/pythonCode/ATBSWPbook/partEight'
for dirpath, dirnames, filenames in os.walk(searchPath):
  print('The current dirpath is ' + ': ' + dirpath)
  for dirname in dirnames:
    print('subdirectory of ' + dirpath + ': ' + dirname)
  for filename in filenames:
    print('file inside ' + dirpath + ': ' + filename)
  print('')
