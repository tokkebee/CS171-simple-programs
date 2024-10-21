#Oliver (Ollie) Kim
#June 5, 2024

#CS171 HW08 Auxiliary List Sort
#This program sorts a list of random numbers between inputted min and max positive integers. It sorts by ones, then tens, then hundreds.
#Important note: doesn't use insertion or quicksort. I think that was the assignment? To make a new sort method?

import random
test = [1, 2, 3]
#this function does the explained sort method
def newSort(list):
    #Part 1: Find biggest value and how many digits it has
    biggest = max(list)
    digits = len(str(biggest))

    #Part 2: Sort by x digit place
    for i in range(digits):
        auxLists = []
        for x in range(10):
            auxLists.append([])
        
        for num in list:
            digit = (num // (10 ** i)) % 10
            auxLists[digit].append(num)
        
        list = []
        for sublist in auxLists:
            for num in sublist:
                list.append(num)
    
    return list

#main
check = False #variable to check input validity

#length and check
#length must be positive int
length = input("How many values do you want in the list? ")
while not str(length).isdigit() or not check:
    if length.isdigit():
        length = int(length)
        if length > 0:
            check = True
        elif length == 0:
            print("Must be a positive integer.")
            length = input("How many values do you want in the list? ")
    elif (length[0] == '-' and str(length[1:]).isdigit()):
        print("Must be a positive integer.")
        length = input("How many values do you want in the list? ")
    else:
         print("Invalid input.")
         length = input("How many values do you want in the list? ")

check = False
#min and check
#min must be positive int
minVal = input("What should be the minimum value? ")
while not str(minVal).isdigit() or not check:
    if minVal.isdigit():
        minVal = int(minVal)
        check = True
    elif minVal[0] == '-' and str(minVal[1:]).isdigit():
        print("Must be a positive integer.")
        minVal = input("What should be the minimum value? ")
    else:
        print("Invalid input.")
        minVal = input("What should be the minimum value? ")

check = False
#max and check
#max must be positive int and greater than min
maxVal = input("What should be the maximum value? ")
while not str(maxVal).isdigit() or not check:
    if maxVal.isdigit():
        maxVal = int(maxVal)
        if maxVal > minVal:
            check = True
        else:
            print("Max value must be greater than min value")
            maxVal = input("What should be the maximum value? ")
    elif maxVal[0] == '-' and str(maxVal[1:]).isdigit():
        print("Must be a positive integer.")
        maxVal = input("What should be the maximum value? ")
    else:
        print("Invalid input.")
        maxVal = input("What should be the maximum value? ")

#list population
list = []
for num in range(length):
    list.append(random.randint(minVal, maxVal))

print(f'Before: {list}')
print(f'After: {newSort(list)}')