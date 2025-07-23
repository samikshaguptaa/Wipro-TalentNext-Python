# 1. Return sum of all numbers in a list
def sumOfNums(num):
    sum = 0
    for i in num:
        sum+=i
    return sum

num = [1,2,3]
print(sumOfNums(num))

# 2. Return reverse of a string
def revString(str):
    return str[::-1]
print(revString("abcd"))

# 3. Return factorial of a number
def factorial(num):
    if num==0 or num==1:
        return 1
    return num * factorial(num-1)
print(factorial(5))

# 4. Count uppercase and lowercase letters
def count(str):
    upper = lower = 0
    for ch in str:
        if ch.isupper():
            upper+=1
        elif ch.islower():
            lower+=1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
count("AAHhdd")

# 5. Print even numbers from list
def evenNums(ls):
    for i in ls:
        if(i%2==0):
            print(i,end=" ")
ls = [2,4,51,9]
evenNums(ls)

#  6. Check if a number is prime
def isPrime(nums):
    if(nums<=1):
        return False
    for i in range(2,int(nums*0.5)+1):
        if nums%i==0:
            return False
        return True
print(isPrime(13))