tableData = [['apples', 'oranges', 'cherries', 'banana'], \
             ['Alice', 'Bob', 'Carol', 'David'], \
             ['dogs', 'cats', 'moose', 'goose']]
def printTable(listV):
  colWidths = [0] * len(listV)
  maxLength = 0
  for i in listV:
    for j in i:
      strLength = len(listV[i][j])
      if strLength > maxLength:
        maxLength = strLength
  listFlip = [[3] for i in range(4)]
  for i in range(len(listV)):
    
