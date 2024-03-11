import math


input = open("4/input.txt").read().split("\n")
#input = open("4/inputExample.txt").read().split("\n")

def getPoints(cards, wins):
    points = 0
    for card in cards:
            if card in wins:
                if(points == 0):
                    points = 1
                else:
                    points *= 2
    return points
    
def GetWinningNumbers(line):
    return[win for win in line.split(":")[1].split("|")[0].strip().split(" ") if win != ""]
def GetCardNumbers(line):
    return [card for card in line.split(":")[1].split("|")[1].strip().split(" ") if card != ""]

#PART 1


def Part1():
    score = 0

    for i, line in enumerate(input):
        winningNumbers = GetWinningNumbers(line)
        cardNumbers = GetCardNumbers(line)

        points = getPoints(cardNumbers, winningNumbers)
        
        score += points
    return score 

print("Part 1:")
print(Part1())

#PART 2

def Part2():

    cardCount = 0
    lines = input
    lineRows = len(input)
    winDictionary = {}
    cardDictionary = {}

    for i, line in enumerate(lines):

        gameIndex = [index for index in [i for i in line.split(":")[0].split(" ") if i != ""]][1]

        winningNumbers = GetWinningNumbers(line)
        cardNumbers = GetCardNumbers(line)
        wins = len([card for card in cardNumbers if card in winningNumbers])

        cardDictionary[gameIndex] = 1
        winDictionary[gameIndex] = wins


    print(cardDictionary)
    print("")

    for i, line in enumerate(lines):
        gameIndex = [index for index in [i for i in line.split(":")[0].split(" ") if i != ""]][1]
        winningNumbers = GetWinningNumbers(line)
        cardNumbers = GetCardNumbers(line)

        wins = len([card for card in cardNumbers if card in winningNumbers])
        winDictionary[gameIndex] = wins
    print(winDictionary)
    print("")

    for game, gameCount in cardDictionary.items():
        
        currentGame = 1
        while currentGame <= gameCount:
            wins = winDictionary[game]
            j = 0
            while j < wins:
                if(int(game) + (j+1) <= lineRows): # kanske <=
                    cardDictionary[str(int(game)+ (j+1))] += 1
                j +=1
            currentGame += 1


    print(cardDictionary)
    print("")
    cardCount = sum(cardDictionary.values())

        
    return cardCount 





print("Part 2:")
print(Part2())



# def Part2(lines, start, stop):
#     sum = 0
#     lineRows = len(input)
#     for i, line in enumerate(lines):
#         winningNumbers = [win for win in line.split(":")[1].split("|")[0].strip().split(" ") if win != ""]
#         cardNumbers = [card for card in line.split(":")[1].split("|")[1].strip().split(" ") if card != ""]
#         #sum += 1

#         wins = len([card for card in cardNumbers if card in winningNumbers])
#         cardIndex = start + i
#         if ( cardIndex < lineRows):
#             part2Result = Part2(input[i+1 : i+wins+1], i+1, i+wins+1)
#             return (1 + part2Result )
#         else:
#             return 0