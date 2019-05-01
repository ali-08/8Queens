import random

''' 
    Data types:
    list for queens Q1-Q8 [NO NEED]
    dict for domains for each queen
    list for board
'''


def placeQueenRandomly(board, queenNum):
    r = random.choice(qD[qMap[queenNum]])
    board[r][queenNum] = qMap[queenNum]
    return r


# places queen on particular position
def placeQueenOnPos(board, queenNum, position):
    r = position
    board[r][queenNum] = qMap[queenNum]
    return r


# Function to print board
def printB(board):
    print("Board:")
    r = len(board[0])
    for i in range(0,r):
        for j in range(0, r):
            if board[i][j] == 0:
                print(board[i][j],  end="  ")
            else:
                print(board[i][j],  end=" ")
        print()


# Function to print the domain of each queen
def printDomain(dic, qMap):
    print("Domain:")
    for i in dic:
        print('Queen', i, dic[i])


# Function to adjust domain; called after a queen is placed
def shrinkDomain(board, qD, qMap, queenNum):
    length = len(board[0])
    pos = 0
    flag = False
    pos1 = 0
    pos2 = 0
    q = queenNum
    # we get to know the row pos of qth queen
    for c in range(0, length):
        if board[c][q] != 0:
            pos = c
            pos1 = pos
            pos2 = pos
            # print('Queen',  q, 'pos', pos)
            flag = True
            break

        # Shrink domain for qth queen
        # print('pos', pos)
        # print('Queen: ', q)
    if flag == True:
            # print('Flag TRUE for Queen:', q)
        for q1 in range(q+1, length):
            # if pos in [x for v in qD.values() for x in v]
            if pos in qD[qMap[q1]]:
                # print(pos)
                qD[qMap[q1]].remove(pos)
                # print(pos)
            pos1 = pos1 - 1
            if pos1 >= 0:
                if pos1 in qD[qMap[q1]]:
                    qD[qMap[q1]].remove(pos1)
            pos2 = pos2 + 1
            if pos2 <= 7:
                if pos2 in qD[qMap[q1]]:
                    qD[qMap[q1]].remove(pos2)
            # print(q1, qD[qMap[q1]])


# autmomatically removes the queen and restores the domain of consequent queens
def restoreDomain(board, qD, qMap, qNum):
    length = len(board[0])
    pos = 0
    pos1 = 0
    pos2 = 0
    flag = False
    # make the pos on board 0
    for c in range(0, length):
        if board[c][qNum] != 0:
            board[c][qNum] = 0
            pos = c
            pos1 = pos
            pos2 = pos
            flag = True
            break
    # add the missing values in domain of consequent queens
    if flag == True:
        # add row num
        for q1 in range(qNum+1, length):
            if pos not in qD[qMap[q1]]:
                qD[qMap[q1]].append(pos)
            # add upper diag values
            pos1 = pos1 - 1
            if pos1 >= 0:
                if pos1 not in qD[qMap[q1]] and pos1 != pos:
                    qD[qMap[q1]].append(pos1)
            # add lower diag values
            pos2 = pos2 + 1
            if pos2 <= 7 and pos2 != pos:
                if pos2 not in qD[qMap[q1]]:
                    qD[qMap[q1]].append(pos2)
            qD[qMap[q1]].sort()
    # adjust domain
    for q1 in range(0, qNum+1):
        shrinkDomain(board, qD, qMap, q1)


def isEmpty(qD):
    for i, j in qD.items():
        # Following if condition is used to detect null list
        if not j: 
            return True
    return False


# main 

num_columns = 8
num_rows = num_columns
board = [[0 for i in range(num_columns)] for j in range(num_rows)]

qD = {
    'Q0' : [i for i in range(num_rows)],
    'Q1' : [i for i in range(num_rows)],
    'Q2' : [i for i in range(num_rows)],
    'Q3' : [i for i in range(num_rows)],
    'Q4' : [i for i in range(num_rows)],
    'Q5' : [i for i in range(num_rows)],
    'Q6' : [i for i in range(num_rows)],
    'Q7' : [i for i in range(num_rows)]
}

qMap = {
    0 : 'Q0',
    1 : 'Q1',
    2 : 'Q2',
    3 : 'Q3',
    4 : 'Q4',
    5 : 'Q5',
    6 : 'Q6',
    7 : 'Q7',
}

qPos = {}

i = 0
error = 0
j = 0

while i < 8:
    qPos[qMap[i]] = placeQueenRandomly(board, i)
    shrinkDomain(board, qD, qMap, i)
    x = isEmpty(qD)
    j = 0
    while x:
        # print('ISEMPTY', x)
        error = error + 1
        restoreDomain(board, qD, qMap, i)
        qPos[qMap[i]] = placeQueenRandomly(board, i)
        shrinkDomain(board, qD, qMap, i)
        j = j + 1
        if error > 3:
            restoreDomain(board, qD, qMap, i)
            error = 0
            i = i - 1
            if j > 12:
                x = False
            # print('IF OF ISEMPTY', i)
            # print(x)

    # restoreDomain(board, qD, qMap, i)
    error = 0
    i = i + 1
    print(i)
printB(board)

# print("Entering Q0")
# i = 0
# qPos[qMap[i]] = placeQueenOnPos(board, i, 4)
# shrinkDomain(board, qD, qMap,i)

# print("Entering Q1")
# i = 1
# qPos[qMap[i]] = placeQueenOnPos(board, i, 6)
# shrinkDomain(board, qD, qMap, i)
# printB(board)

# print("Removing Q1")
# restoreDomain(board, qD, qMap, i)
# printB(board)
# printDomain(qD, qMap)

# print(qPos)





