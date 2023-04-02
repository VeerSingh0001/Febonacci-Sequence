# This is a program of printing Fibonacci Sequence.

def feboseq(value): # Function for printing sequence
    firstnum = 0
    secondnum = 1
    if value == 1:
        print(firstnum)
    elif value <= 0:
        print("Please enter a value greater than 0!")
    else:
        print(firstnum, secondnum, end=" ")
        for i in range(2, value):
            result = firstnum + secondnum
            firstnum,secondnum = secondnum,result
            print(result, end=" ")

values = int(input("Enter the values you want to print: "))
feboseq(values)
