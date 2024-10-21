#Oliver (Ollie) Kim
#May 1, 2024

#CS171 HW04 Binary to Integer
#This program converts binary numbers to integers
#program only accepts inputs in valid formats

#function: checks if input is binary
def getBinary():
    binary = input("Enter a binary number: ")
    check = False
    while not check: #loops until "return binary"
        if binary.replace("1", "").replace("0","") == "": #removes 1's and 0's. s.replace() can technically infinitely stack
            return binary
        else:
            print("Not a binary number. Please try again.")
            binary = input("Enter a binary number: ")

#function: outputs decimal equivalent to binary input
def stringToBinary(binary):
    decimal = 0
    power = len(binary) - 1
    i = 0
    while i < len(binary):
        if binary[i] == '1': #'1' because binary is string
            decimal += 2 ** power
        power -= 1
        i += 1
    return decimal
    

#program start
print("Welcome to Binary Converter")

#program loop
confirm = 'y'
while confirm.lower() == 'y': #assumes user will not answer outside y/Y or n/N
    binary = getBinary()
    decimal = stringToBinary(binary)
    print(f"The decimal equivalent of {binary} is: {decimal}\n")
    confirm = input("Do you want to convert another binary number (Y/N)? ")

print("Ok, goodbye.")