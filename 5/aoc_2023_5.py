import math
import sys
import re


input = open("5/input.txt").read()
#input = open("5/inputExample.txt").read()


def ProcessMap( stringMap):
    rows = str(stringMap).split("\n")
    processedRows = []
    for row in rows:
        stringRow = row.split(" ")
        if(len(stringRow) > 1):
            intRow = [int(x) for x in stringRow]
            processedRows.append(intRow)
    return processedRows

def MapToDict(listMap):
    myDict = {}
    for mapping in listMap:
        for i in range(mapping[2]):
            myDict[str(mapping[1] + i )] = str(mapping[0] + i)
    return myDict

def MapToDict2(listMap):
    myDict = []
    #print(listMap)
    for mapping in listMap:
        #print(mapping)
        myDict.append(( range(mapping[1], mapping[1]+mapping[2]), range(mapping[0], mapping[0]+mapping[2])) )
    #print(myDict)
    return myDict

listOfSeedsAndMaps = re.split("seeds:\n|seed-to-soil map:\n|soil-to-fertilizer map:\n|fertilizer-to-water map:\n|water-to-light map:\n|light-to-temperature map:\n|temperature-to-humidity map:\n|humidity-to-location map:\n", input)
seeds = re.split(" |\n" ,listOfSeedsAndMaps[0].split(":")[1])
seeds.remove("")
seeds = seeds[: len(seeds)-2]
seeds = [int(x) for x in seeds]
#print(seeds)

seedToSoilMap =             MapToDict2(ProcessMap(listOfSeedsAndMaps[1]))
#print(seedToSoilMap)
soilToFertilizerMap =       MapToDict2(ProcessMap(listOfSeedsAndMaps[2]))
fertilizerToWaterMap =      MapToDict2(ProcessMap(listOfSeedsAndMaps[3]))
#print(fertilizerToWaterMap)
WaterToLightMap  =          MapToDict2(ProcessMap(listOfSeedsAndMaps[4]))
lightToTemperatureMap =     MapToDict2(ProcessMap(listOfSeedsAndMaps[5]))
temperatureToHumidityMap =  MapToDict2(ProcessMap(listOfSeedsAndMaps[6]))
humidityToLocationMap =     MapToDict2(ProcessMap(listOfSeedsAndMaps[7]))

allMaps = [seedToSoilMap, soilToFertilizerMap, fertilizerToWaterMap, WaterToLightMap, lightToTemperatureMap, temperatureToHumidityMap, humidityToLocationMap]


print("preproccess done")
#PART 1

def Part1(seedList):
    minLocation = 9999999999999999999
    for seed in seedList:
        pushValue = seed
        #print(pushValue)

        for mapping in allMaps:
            foundRange = False
            for mapRange in mapping:

                if pushValue in mapRange[0]:
                    #print("pushValue " + str(pushValue) + " is contained in range")
                    foundRange = True
                    abovebase = pushValue - mapRange[0][0]
                    pushValue = mapRange[1][abovebase]
                    break
            if foundRange == False:
                pushValue = pushValue

            #print(pushValue)

        #print("")

        if pushValue < minLocation:
            minLocation = pushValue


        

    return minLocation


print("Part 1:")
print(Part1(seeds))

#PART 2

def Part2():

    minLocation = 9999999999999999999
    seednumber = 0
    while seednumber < len(seeds):
        
        minSeedLocation = Part1(range(seeds[seednumber], seeds[seednumber] + seeds[seednumber+1])) # TO SLOW

        if minSeedLocation < minLocation:
            minLocation = minSeedLocation
        
        seednumber +=2


 
        
    return minSeedLocation





print("Part 2:")
print(Part2())

