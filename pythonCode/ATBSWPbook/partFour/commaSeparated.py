def comma(strVariable):
  #print(type(listVariable))
  listVariable = strVariable.split(",")  
  strVariable = ""
  for i in range(len(listVariable)):
    print(i)
    if i != (len(listVariable) - 1): 
      strVariable += str(listVariable[i]) + ","
    else:
      strVariable += "and " + str(listVariable[i])
  return strVariable
myList = input()
print(comma(myList))
