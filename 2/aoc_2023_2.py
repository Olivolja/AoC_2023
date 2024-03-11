import math

input = open("2/input.txt").read().split("\n")
#input = open("2/inputExample.txt").read().split("\n")

listofColors = ["red", "blue", "green"]

#PART 1
maxRed = 12
maxBlue = 14
maxGreen = 13
sum = 0
for line in input:

    game = line.split(":")
    gameNumber = int(game[0].split(" ")[1])
    turns = game[1].split(";")
    isGamePossible = False

    for turnText in turns:
        turn = turnText.split(",")

        for setofColor in turn:
            amountAndColor = setofColor.strip().split(" ")
            amount = int(amountAndColor[0])
            color = amountAndColor[1]

            if (color == "red" and amount <= maxRed):
                isGamePossible = True
            elif (color == "blue" and amount <= maxBlue):
                isGamePossible = True
            elif (color == "green" and amount <= maxGreen):
                isGamePossible = True
            else: 
                isGamePossible = False
                #print ("game " + game[0].split(" ")[1] + " is false"  )
                break

        if (isGamePossible == False):
            break

    if (isGamePossible):
        #print(gameNumber)
        sum += gameNumber
        isGamePossible = False

print("Part 1:")
print(sum)


#PART 2

maxRed = 12
maxBlue = 14
maxGreen = 13
sum = 0
for line in input:

    game = line.split(":")
    gameNumber = int(game[0].split(" ")[1])
    turns = game[1].split(";")

    minRed = 0
    minBlue = 0
    minGreen = 0
    for turnText in turns:
        turn = turnText.split(",")

        for setofColor in turn:
            amountAndColor = setofColor.strip().split(" ")
            amount = int(amountAndColor[0])
            color = amountAndColor[1]

            if (color == "red"):
                if (amount > minRed):
                    minRed = amount
            elif (color == "blue" ):
                if (amount > minBlue):
                    minBlue = amount
            elif (color == "green" ):
                if (amount > minGreen):
                    minGreen = amount

    #get power
    power = minRed * minBlue * minGreen
    #add to sum
    sum += power

    
print("Part 2:")
print(sum)