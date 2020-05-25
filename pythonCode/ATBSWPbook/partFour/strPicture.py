import copy
grid = [[".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", "0", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        [".", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]
def flip(grid):
  listX = []
  listY = []
  for x in range(len(grid[0])):
    for y in range(len(grid)):
      #gridCopy = copy.copy(grid) 
      listX.append(grid[y][x])
    listY.append(listX)
    listX = []
  return listY

flipOut = flip(grid)
#for i in range(len(grid)):
  #print(flipOut[i])
for i in range(len(flipOut)):
  str = ""
  for j in range(len(flipOut[i])):
    str = flipOut[i][j] + str
  print(str, "\n")
  str = ""

