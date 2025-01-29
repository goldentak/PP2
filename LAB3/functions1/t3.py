# 3  |  Write a program to solve a classic puzzle

def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads)/2
    chickens = numheads - rabbits
    return chickens, rabbits


headcount = 35
legcount = 94
print(solve(headcount, legcount))