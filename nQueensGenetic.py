# K16-3637      K16-3633

import random
from heapq import nsmallest 

# Function to print list
def printl(l):
    length = len(l)
    for i in range(0, length):
        print(l[i])


# Function that calculates fitness; 0 means that not a single attacking pair of queen exists
def fitnessFunc(l):
    length = len(l)
    c = 0
    for i in range(0, length):
        currentPos = l[i]
        ud = l[i]
        ld = l[i]
        for j in range(i+1, length):
            if currentPos == l[j]:
                c = c + 1
            if ud >= 1:
                ud = ud - 1
                if ud == l[j]:
                    c = c + 1
            if ld <= 8:
                ld = ld + 1
                if ld == l[j]:
                    c = c + 1
    return c


# Crossover that takes first 4 bits from first parent and remaining 4 bits from second parent and vice versa
# this crossover is unable to provide solution
def crossover(l):
    children = [[None for _ in range(8)] for _ in range(4)]
    # children of l1 and l2
    i = 0
    x = 0
    y = 7
    # 1st child
    while x < 4:
        children[i][x] = l[i][x]
        children[i][y] = l[i+1][y]
        x = x + 1
        y = y - 1
    # 2nd child
    i = 1
    x = 0
    y = 7
    while x < 4:
        children[i][x] = l[i][x]
        children[i][y] = l[i-1][y]
        x = x + 1
        y = y - 1

    # 3rd child
    j = 2
    x = 0
    y = 7
    while x < 4:
        children[j][x] = l[j-1][x]
        children[j][y] = l[j][y]
        x = x + 1
        y = y - 1
    # 4th child
    j = 3
    x = 0
    y = 7
    while x < 4:
        children[j][x] = l[j-1][x]
        children[j][y] = l[j-2][y]
        x = x + 1
        y = y - 1

    return children


# This crossover choses bits in offspring randomly from 2 parents but ensures non repeating bits to get the solution
def crossover2(parent):
    children = [[], [], [], []]
    i = 0
    c = 0
    j = 7

    while len(children[0]) < 8:
        pos = random.randint(0,7)
        if parent[0][pos] not in children[0]:
            children[0].append(parent[0][pos])
        pos1 = random.randint(0,7)
        if parent[1][pos1] not in children[0]:
            children[0].append(parent[1][pos1])

    while len(children[1]) < 8:
        pos = random.randint(0,7)
        if parent[1][pos] not in children[1]:
            children[1].append(parent[1][pos])
        pos1 = random.randint(0,7)
        if parent[0][pos1] not in children[1]:
            children[1].append(parent[0][pos1])

    while len(children[2]) < 8:
        pos = random.randint(0,7)
        if parent[1][pos] not in children[2]:
            children[2].append(parent[1][pos])
        pos1 = random.randint(0,7)
        if parent[2][pos1] not in children[2]:
            children[2].append(parent[2][pos1])

    while len(children[3]) < 8:
        pos = random.randint(0,7)
        if parent[2][pos] not in children[3]:
            children[3].append(parent[2][pos])
        pos1 = random.randint(0,7)
        if parent[1][pos1] not in children[3]:
            children[3].append(parent[1][pos1])

    return children


# choose random position of bits randomly from one of four children
def mutation(l):
    listMutated = random.randint(0, 3)
    swapPos1 = random.randint(0, 7)
    swapPos2 = random.randint(0, 7)

    temp = l[listMutated][swapPos1]
    l[listMutated][swapPos1] = l[listMutated][swapPos2]
    l[listMutated][swapPos2] = temp

    return l


# main

l = [[i for i in range(1,9)],
     [i for i in range(1,9)],
     [i for i in range(1,9)],
     [i for i in range(1,9)]]

fitnessD = {}
fitnessPerfect = {}

x = 0
generations = 500
c = 0
while x < generations:
    for i in range(0,4):
        random.shuffle(l[i])
        fitnessD[i] = fitnessFunc(l[i])

    # for x, y in fitnessD.items():
    #     print(x, y) 


    minFitness = []
    # Choose 3 chromosomes with with best(min) fitness value
    # three has all the indexes of min fitnesses
    # three is a list
    three = nsmallest(3, fitnessD, key = fitnessD.get)
    # pich the indexes of min fitness func
    for val in three:
        # print(val, fitnessD.get(val))
        minFitness.append(val)
    
    length = len(minFitness)
    selected = []
    for i in range(0, length):
        selected.append(l[minFitness[i]])

    children = crossover2(selected)

    children = mutation(children)

    l = children
    x = x + 1

    # stores generation number as index in dict
    for i in range(0,4):
        # print(fitnessFunc(children[i]))
        if fitnessFunc(children[i]) == 0:
            print('Generation:', x, "   ", children[i])



'''
Python Code:

from heapq import nlargest
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest) 

 

Copy

Sample Output:

['e', 'b', 'c']

'''