# Write a python function to print the table of given user input
def table():
    number = int(input("Enter a number:  "))
    for i in range(1,13):
        print(f"{number} * {i} = {number * i}")

table()
