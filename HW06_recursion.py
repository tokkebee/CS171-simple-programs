#Oliver (Ollie) Kim
#May 16, 2024

#CS171 HW06 Recursion
#This program has three recursive functions, which outputs dot product, index of inquired element, and biggest number in the inputted number's Collatz sequence, respectively.

#Part 1: The Dot Product
#this function looks at two lists and outputs the dot product. If lists aren't the same size, output is 0.
def  dotProduct(list1, list2):
    if len(list1) != len(list2): # unequal list check
        return 0.0
    elif len(list1) == 0 or len(list2) == 0: #when either list is empty, exit
        return 0.0
    else:
        product = list1[0] * list2[0]
        return dotProduct(list1[1:], list2[1:]) + product

#Part 2: Finding Elements
#this function searches container for element and if found, outputs the index number. Otherwise, returns the size of the container
def findPosition(container, element):
    container = list(container)
    if element not in container: #return size if not found
        return len(container)
    if container[0] == element:
        return 0
    index = findPosition(container[1:], element)
    return index + 1

#example
#print(findPosition('Honestly, thats crazy', ','))
#output = 8

#Part 3: The Collatz Sequence
#this function does the Collatz sequence on an inputted integer and then returned the highest integer in that sequence.

def maxCollatz(number):
    def collatzSeq(num, seq, maxVal): 
        if num == 1:
            return maxVal
        else:
            if num % 2 == 0:
                num //= 2
            else:
                num = (num * 3) + 1
            maxVal = num if num > maxVal else maxVal #one line for legibility
            return collatzSeq(num, seq + [num], maxVal)

    sequence = collatzSeq(number, [number], number)
    return sequence
#example
#print(maxCollatz(10))
#output = 16