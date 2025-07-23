# program to check if number is positive. negetive or zero
num = int(input("Enter a number: "))
if(num>0):
    print("positive")
elif(num<0):
    print("negative")
else:
    print("zero")

# program to check if number is odd or even
num = int(input("Enter a number: "))
if(num%2==0):
    print("even")
else:
    print("odd")

#
def LastDigit(num1,num2):
    if(num1%10 == num2%10):
        print(True)

LastDigit(9,19)

#
for i in range(1,10):
    print(i,end = " ")

#
for i in range(23,58):
    if(i%2==0):
        print(i)

#
num = int(input("Enter a number: "))

if num <= 1:
    print(False)
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(False)
            break
    else:
        print(True)

#
for num in range(10, 100):  # from 10 to 99
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

#
num = int(input("Enter a number: "))
sum = 0
while(num):
    sum+=num%10
    num=num/10
print(sum)

#
num = int(input("Enter a number: "))
res = 0
while(num):
    digit=num%10
    res = res * 10 + digit
    num=num/10
print(res)

#
num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("Palindrome")
else:
    print("Not a palindrome")