#Advent of Code 2015 Day 1


santaGpsInput = input("Enter the Required GPS Detail: ")

floor = 0
satanCurrentFloor =0

for letter in santaGpsInput:
    if(letter == "("): 
        floor +=1
        satanCurrentFloor += 1
    elif (letter == ")"): 
        floor -=1
        satanCurrentFloor += 1
    if floor == -1:
        print("Santa have arrived at the basement!", satanCurrentFloor, "\nSanta current floor",floor)
        break