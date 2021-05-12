weight = int(input("Enter you weight "))
standerd = input("(K)g or (L)bs ").upper()
weightInKg = weight * 0.45
weightInPounds = weight * 2.20462
if(standerd == "L"):
  print("your weight in Kg is "+ str(weightInKg))
elif(standerd == "K"):
  print("You weight in Pound is " + str(weightInPounds))



# Program to reverse a number 
num = list(str(123456))
def reverseNumber(num) :
  reverse = ''
  for i in range(len(num)-1,-1,-1):
    reverse += num[i] 
  print(reverse)

reverseNumber(num)

# Sum of elements in an array
num = str(1234)

def sumOfElements(num):
  s = 0
  for i in range (0,len(num),1):
    s = s + int(num[i])
  print(s)
sumOfElements(num)

# Duplicated in an array
arr = [1,2,3,4,5,2,3,4,2,1]

arr1 = list(set(arr))
print(arr1)

# Second Largest number in an array
arr1 = [1,2,3,21,23,222]
arr1.remove(max(arr1))
print(max(arr1))

# Write a function to print all the elements whose value is a multiple of 3 and multiple of 5

a = [1,2,3,4,5,6,7,8,9,10,15,20,22,23,45,65,34,41,43,47]

def multThreeFive (num) :
  for i in range (0,len(num)):
    if(num[i]%3 == 0 and num[i]%5 == 0):
      print(num[i])

multThreeFive(a)

# Declare 2 arrays of the same size and print the values of both using one for loop
a = [1,2,3,4,5]
b = [2,3,4,5,6]

def sumofTwoArray (num1,num2):
  s = 0
  for i in range (0 ,len(num1)):
    s = num1[i] + num2[i]
    print(s) 

sumofTwoArray(a,b)

# pallindrome
a = input("Enter the sentence or number wheather to check if it is a pallindrom or not ")

def pallindrome(num): 
  for i,j in range(0,len(num),1), range(len(num)-1,-1,-1):
    if(num[i] == num[j]):
      print("Its a pallindrome")
    else:
      print("not pallindrome")

pallindrome(a)

# Check the given number is prime or not 

a = int(input("Enter the number"))

def primNumber(a) :
  for i in range(2,a):
    if(a%i == 0):
      print("its not a prime number")
      break
  else:
    print("Its a Prime Number")

primNumber(a)   

# check for a range of prime numbers
for i in range(1,100):
  if i > 1:
    for num in range(2,i):
      if(i%num == 0):
        break
    else:
      print(i)

# Amstrong Number
for i in range(1,1001):
  num = i
  result = 0
  n = len(str(i))
  while(i!=0):
    digit = i%10
    result = result+ digit**n
    i = i//10
  if(num == result):
    print(num)

# check if a num is amstrong or not
num = int(input('Enter the number'))
i = num
result = 0
n = len(str(num))
while(num!=0):
  digit = num % 10
  result = result + digit**n
  num = num//10
if(i == result):
  print("The Entered number is Amstrong")
else:
  print("Enterd number is not Amstrong")

# fibonacci series
n = int(input("Enter the count for the series"))
first = 0
second = 1
for i in range(n):
  print(first)
  temp = first
  first = second
  second = temp + first

def fibonacci (num) :
  first  = 0 
  second = 1
  for i in range (num):
    print(first)
    temp = first 
    first = second
    second = temp + first

fibonacci(5)

def reverseNum (num):
  reverse = ''
  for i in range(len(num)-1,-1,-1):
    reverse = reverse

