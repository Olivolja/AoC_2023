import math

#input = open("3/input.txt").read().split("\n")
input = open("3/inputExample.txt").read().split("\n")


#PART 1
sum = 0
grid = []

#Prepare data
for i, row in enumerate(input):
    rowValues = list(row)
    grid.append(rowValues)
    #print(rowValues)


#data prepared
rowLength = len (grid[0])
columnLength = len (grid)

checkedGrid = []
for row in grid:
    checkedGrid.append(["0"]*rowLength)


for i, row in enumerate(grid):
    for j, value in enumerate(row):

        if( str(value).isnumeric() or str(value) == "."):
            continue

        else: #special symbol
            checkRows = range(i-1, i+2)
            checkColumns = range(j-1, j+2)
            #print(value)
            for rowToCheck in checkRows:
                for columnToCheck in checkColumns:
                    if(rowToCheck >= 0 and rowToCheck < rowLength and columnToCheck >= 0 and columnToCheck < columnLength ): #inside grid and not inside checkedGrid
                        if(str(grid[rowToCheck][columnToCheck]).isnumeric()):
                            if(str(checkedGrid[rowToCheck][columnToCheck]).isnumeric() == False):
                                continue
                            valueToAdd = ""

                            checkIndex = columnToCheck
                            while (checkIndex >= 0 and str(grid[rowToCheck][checkIndex]).isnumeric() and str(checkedGrid[rowToCheck][checkIndex]).isnumeric()):
                                if(str(checkedGrid[rowToCheck][checkIndex]).isnumeric() == False):
                                    checkIndex -= 1
                                    continue
                                checkedGrid[rowToCheck][checkIndex] = "X"
                                valueToAdd = str(grid[rowToCheck][checkIndex]) + valueToAdd
                                checkIndex -= 1

                            checkIndex = columnToCheck + 1
                            while (checkIndex < columnLength and str(grid[rowToCheck][checkIndex]).isnumeric() and str(checkedGrid[rowToCheck][checkIndex]).isnumeric()):
                                if(str(checkedGrid[rowToCheck][checkIndex]).isnumeric() == False):
                                    checkIndex += 1
                                    continue
                                checkedGrid[rowToCheck][checkIndex] = "X"
                                valueToAdd =  valueToAdd + str(grid[rowToCheck][checkIndex])
                                checkIndex += 1

                            sum += int(valueToAdd)    

print("Part 1:")
print(sum)

for row in checkedGrid:
    print(row)


#PART 2
sum = 0
grid = []

#Prepare data
for i, row in enumerate(input):
    rowValues = list(row)
    grid.append(rowValues)
    #print(rowValues)


#data prepared
rowLength = len (grid[0])
columnLength = len (grid)

checkedGrid = []
for row in grid:
    checkedGrid.append(["0"]*rowLength)


for i, row in enumerate(grid):
    for j, value in enumerate(row):

        if( str(value).isnumeric() or str(value) == "."):
            continue

        else: #special symbol
            checkRows = range(i-1, i+2)
            checkColumns = range(j-1, j+2)
            valuesToAdd = []
            #print(value)
            for rowToCheck in checkRows:
                for columnToCheck in checkColumns:
                    if(rowToCheck >= 0 and rowToCheck < rowLength and columnToCheck >= 0 and columnToCheck < columnLength ): #inside grid and not inside checkedGrid
                        if(str(grid[rowToCheck][columnToCheck]).isnumeric()):
                            if(str(checkedGrid[rowToCheck][columnToCheck]).isnumeric() == False):
                                continue
                            valueToAdd = ""

                            checkIndex = columnToCheck
                            while (checkIndex >= 0 and str(grid[rowToCheck][checkIndex]).isnumeric() and str(checkedGrid[rowToCheck][checkIndex]).isnumeric()):
                                if(str(checkedGrid[rowToCheck][checkIndex]).isnumeric() == False):
                                    checkIndex -= 1
                                    continue
                                checkedGrid[rowToCheck][checkIndex] = "X"
                                valueToAdd = str(grid[rowToCheck][checkIndex]) + valueToAdd
                                checkIndex -= 1

                            checkIndex = columnToCheck + 1
                            while (checkIndex < columnLength and str(grid[rowToCheck][checkIndex]).isnumeric() and str(checkedGrid[rowToCheck][checkIndex]).isnumeric()):
                                if(str(checkedGrid[rowToCheck][checkIndex]).isnumeric() == False):
                                    checkIndex += 1
                                    continue
                                checkedGrid[rowToCheck][checkIndex] = "X"
                                valueToAdd =  valueToAdd + str(grid[rowToCheck][checkIndex])
                                checkIndex += 1

                            valuesToAdd.append(int(valueToAdd))

            #check if two values to add
            if(len(valuesToAdd) == 2):
                sum += valuesToAdd[0] * valuesToAdd[1]
    
print("Part 2:")
print(sum)


