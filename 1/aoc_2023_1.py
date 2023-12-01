import math

input = open("1/input.txt").read().split("\n")
#input = open("1/inputExample.txt").read().split("\n")


#PART 1
sum  = 0
for line in input:
    firstNumber = "0"
    secondNumber = "0"
    isFirst = True
    i = 0
    while i < len(line):         
        if (line[i].isnumeric()):
            if(isFirst):
                firstNumber = line[i]
                secondNumber = line[i]
                isFirst = False
            else:
                secondNumber = line[i]
        i+=1
    concatenatedNumber = firstNumber + secondNumber
    sum += int(concatenatedNumber)
print("Part 1:")
print(sum)

#PART 2
sum = 0
listOfNumbersAsWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in input:
    firstNumber = "0"
    secondNumber = "0"
    isFirst = True
    i = 0

    currentWord = ""
    while i < len(line):      
        if (line[i].isnumeric()):
            currentWord = "" # Reset currentWord since we found a number
            if(isFirst):
                firstNumber = line[i]
                secondNumber = line[i]
                isFirst = False
            else:
                secondNumber = line[i]
        else:
            currentWord += line[i] #build string to word
            for j, word in enumerate(listOfNumbersAsWords):
                if(word in currentWord[-5:]): # [-5:] only use the last 5 letters in the word otherwise "onetwothree" string would return "one" but we want "theee"
                    if(isFirst):
                        firstNumber = str(j+1) #j+1 since j starts at 0
                        secondNumber = str(j+1)
                        isFirst = False
                    else:
                        secondNumber = str(j+1)
                        
        i+=1
    concatenatedNumber = firstNumber + secondNumber
    sum += int(concatenatedNumber)
print("Part 2:")
print(sum)

