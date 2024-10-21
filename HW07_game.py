#Oliver (Ollie) Kim
#May 28, 2024

#CS171 HW07 Game
#This program is a basic dice game, where 2 players roll 5 dice each. Scores for singles, three of a kind, four of a kind, five of a kind, full house, and straight. Seven functions
#assumes given list will only has integers from 1 to 6, inclusive

import random #dice roll

#Part 1: Singles
#this function checks if a list has a number and returns the sum of all instances (if 3 appears twice, output is 6)
def  checkSingles(list, goal):
    result = 0
    for num in list:
        if num == goal:
            result += num
    return result
#print(checkSingles([2, 6, 1, 1, 4, 4, 2, 6, 2, 6], 2) )

#Part 2: Three of a Kind
#this function outputs 30 if the given list has 3 instances of a number
def checkThreeOfKind(list):
    count = [0,0,0,0,0,0]
    for num in list:
        if num <= 6:
            count[num-1] += 1
    if 3 in count: #just 3 is ok because theres only 5 dice (di?)
        return 30
    return 0
#print(checkThreeOfKind([3, 1, 3, 6, 3]))

#Part 3: Four of a Kind
#this function outputs 40 if the given list has 4 instances of a number
def checkFourOfKind(list):
    count = [0,0,0,0,0,0]
    for num in list:
        if num <= 6:
            count[num-1] += 1
    if 4 in count: #just 3 is ok because theres only 5 dice (di?)
        return 40
    return 0
#print(checkFourOfKind([1, 4, 1, 3, 1, 1, 4]) )

#Part 4: Five of a Kind
#this function outputs 50 if the given list has 5 instances of a number
def checkFiveOfKind(list):
    count = [0,0,0,0,0,0]
    for num in list:
        if num <= 6:
            count[num-1] += 1
    if 5 in count: #just 3 is ok because theres only 5 dice (di?)
        return 50
    return 0
    # list = sorted(list)
    # for num in range(len(list) - 3):
    #     if list[num] == list[num + 1] == list[num + 2] == list[num + 3] == list[num + 4]:
    #         return 50
    # return 0
#print(checkFiveOfKind([4, 4, 2, 4, 1, 2, 4, 4, 1, 1]) )

#Part 5: Full House
#this function outputs 35 if the given list has a pair and three of a kind
def checkFullHouse(list):
    count = [0,0,0,0,0,0]
    for num in list:
        if num <= 6:
            count[num-1] += 1
    if (2 in count) and (3 in count): #just 3 is ok because theres only 5 dice (di?)
        return 35
    return 0
#print(checkFullHouse([3, 3, 2, 6, 6, 6, 1, 4]))

#Part 6: Straight
#this function outputs 45 if list contains a straight (all elements are consecutive)
def checkStraight(list):
    list = sorted(list)
    check = True
    for num in range(len(list) - 2):
        if list[num] != list[num + 1] - 1:
            check = False
    if check:
        return 45
    else:
        return 0
#print(checkStraight([1, 2, 3, 5, 6]))

#Part 7: High Score
#this function returns the category and score of the highest scoring category
def findHighScore(list):
    scores = ['TEMP',checkThreeOfKind(list),checkFourOfKind(list),checkFiveOfKind(list),checkFullHouse(list),checkStraight(list)] #singles, 3, 4, 5 of a kind, full house, straight
    categories = ['Singles', 'Three of a Kind', 'Four of a Kind', 'Five of a Kind', 'Full House', 'Straight']
    
    #checking for biggest singles score
    singles = []
    for num in range(6):
        singles.append(checkSingles(list,(num + 1)))
    scores[0] = max(singles) #replacing scores temp

    return [max(scores), categories[scores.index(max(scores))]]
#print(findHighScore([6, 6, 6, 5, 6]))

#Part 8: Main
party = [[],[]] # highest score
for player in range(2):
    print(f'Player {player + 1}\n-----------')
    #5 random dice rolls
    for dice in range(5):
        dice = random.randint(1,6)
        print(f'Dice: {dice}')
        party[player].append(dice)
    #highest score of the player
    score, category = findHighScore(party[player])
    print(f'\nCategory: {category}')
    print(f'High Score: {score}\n')
    #save player's score
    party[player] = score

print(f'-----------\nPlayer {party.index(max(party)) + 1} wins!')