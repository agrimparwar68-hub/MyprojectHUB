# Write a python function to print the table of given user input
def table():
    number = int(input("Enter a number:  "))
    for i in range(1,13):
        print(f"{number} * {i} = {number * i}")

table()

#rewrite table function using while loop
def table2():
    number1 = int(input("Enter a number"))
    i = 1
    while i <= 12:
        print(f"{number1} * {i} = {number1 * i}")
        i+=1

table2()
