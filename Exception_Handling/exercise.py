#  1. Accept two numbers and perform division
try:
    num1 = int(input("Enter 1st num: "))
    num2 = int(input("Enter 1st num: "))
    res = num1/num2
    print(res)
except Exception as e:
    print("exception : ", e)

# 2. Accept a number and check if it's prime (handle non-numeric input)
try:
    num = int(input("Enter a number: "))
    while(num<=1):
        print("Not prime")
    for i in range(2,(num*num)+1):
        if num%i==0:
            print("Not prime")
            break
        else:
            print("Prime")
except ValueError:
    print("Invalid input! Please enter a valid number.")

#3. Write a program to accept the file name to be opened from the user, if file exists print the contents of the file in title case or else handle the exception and print an error message.
try:
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        content = file.read()
        print(content.title())
except Exception as e:
    print("Error:", e)

#4.Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. If any invalid index is entered, handle the exception and print an error message.
numbers = [10, -5, 7, -3, 15, -9, 0, 8, -2, 4]

try:
    index = int(input("Enter an index (0-9): "))
    value = numbers[index]
    if value > 0:
        print("Positive number")
    elif value < 0:
        print("Negative number")
    else:
        print("Zero")
except Exception as e:
    print("Error:", e)
