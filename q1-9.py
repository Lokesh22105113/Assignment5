#ques1
"""Program to reverse the string."""
string=input("enter the string:")
print(string[::-1])


#ques2
number=int(input("enter a number:"))
n=int(input("enter the range:"))
lists=[]
for i in range(1,n+1):
    if i%number==0:
        lists.append(i)
print(lists)


#ques3
import math
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is:",round(area,2)



      #ques4
# """Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *

for i in range(5):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')




#ques5
# """Write a python program to print a triangular pattern of the alphabet (user input the number of rows).
# Example: Input the number of rows = 5, then the pattern should come out as given below.
# If the count of the alphabet gets exhausted, repeat the alphabet from A.
# A
# BC
# DEF
# GHIJ
# KLMNO"""

rows=int(input("enter number of rows"))
count=0
for i in range(rows+1):
    for j in range(i):
        if count>=26:
            count=0
        print(chr(65+count),end="")
        count+=1
    print()



# ques6
# ""Write a python program to print the prime numbers for a user input range."""

lower_limit=int(input("Enter the lower limit:"))
upper_limit=int(input("Enter the upper limit:"))
for num in range(lower_limit,upper_limit+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)



#ques7
# """Write a python program to find the numbers which are multiple of 7 and divisible by 11 in the range
# 1-500."""
list1=[]
for i in range(1,501):
    if i%7==0 and i%5==0:
        list1.append(i)
print(list1)

#ques8
# """Write a python program to find the numbers which are multiple of 7 and divisible by 11 in the range
# 1-500."""
list1=[]
for i in range(1,501):
    if i%7==0 and i%5==0:
        list1.append(i)
print(list1)



#ques9
# """Write a program to count the number of occurrences of each word in the list(List entered by the user)."""
string=input("Enter string:")
word=input("Enter word:")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
      if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count)
