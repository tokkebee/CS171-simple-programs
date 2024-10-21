def populateSquare(size):
    square = []
    for i in range(size):
        row = [0] * size
        square.append(row)
    return square

def printSquare(square):
    for row in square:
        for value in row:
            print(f'{value}\t', end="")
        print("")

def isMagicSquare(square):
    rowCheck = True
    columnCheck = True
    diaCheck = True
    magicNumber = sum(square[0])
    diaMagicNum01 = 0
    diaMagicNum02 = 0

    #check loop
    for row in range(len(square)):
        #row check
        if sum(square[row]) != magicNumber:
            rowCheck = False
        #column check
        columnMagicNum = 0
        for index in range(len(square[row])):
            columnMagicNum += square[row][index]
        if columnMagicNum != magicNumber:
            columnCheck = False
        #diagonal check
        diaMagicNum01 += square[row][row]
        diaMagicNum02 += square[row][-1 - row]

    if diaMagicNum01 != magicNumber or diaMagicNum02 != magicNumber:
        diaCheck = False

    return rowCheck and columnCheck and diaCheck

#program start
print("Welcome to the Magic Square Game")

#size input and check
size = input("Enter the size of your square (between 3 and 9): ")
check = False
while not str(size).isdigit() or not check:
    if size.isdigit():
        size = int(size)
        if not (3 <= size <= 9):
            print("Value is out of bounds. Please try again.")
            size = input("Enter the size of your square (between 3 and 9): ")
        else:
            check = True
    else:
        print("Invalid input. Please try again.")
        size = input("Enter the size of your square (between 3 and 9): ")

#making empty square
square = populateSquare(size)

#row input and check
dupeCheck = [] #list of previous entered values
for row in range(len(square)):
    print(f"Row {row + 1}")
    for index in range(len(square[row])):
        value = input("Enter a value for the square: ")
        check = False
        while not str(value).isdigit() or not check:
            if value.isdigit():
                value = int(value)
                if not (1 <= value <= size**2):
                    print("Value is out of bounds. Please try again.")
                    value = input("Enter a value for the square: ")
                elif value in dupeCheck:
                    print("Value already in the square. Please try again.")
                    value = input("Enter a value for the square: ")
                else:
                    square[row][index] = int(value)
                    dupeCheck.append(value)
                    check = True 
            else:
                print("Invalid input. Please try again.")
                value = input("Enter a value for the square: ")

#results!
print("\nHere is your square: ")
printSquare(square)

magic = isMagicSquare(square)
if magic:
    print("This is a magic square!")
else:
    print("This is not a magic square.")