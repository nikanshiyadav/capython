"""1. Write a program using function USINto reverse a string. 

Sample data: “1234abcd” 

Expected Output: “dcba4321” """

def revrseString(x):
    return x[::-1]

revText = revrseString("123abcd")
print(revText)   


"""2. Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters. """
def countLetter(x):
    upperCase = 0
    lowerCase = 0

    for l in x:
        if l.isupper():
            upperCase +=1
        elif l.islower():
            lowerCase +=1
        else:
            pass
        print('No: of Upper case letters: ', upperCase)
        print('No. of lower case letters: ', lowerCase)
countLetter('This is a TEST string')                    

"""3. Create a function that takes a list and returns a new list with unique elements of the first list"""
a = ['a','b',2,2,2,3,3,3,'two']
def unique(s):
    b = []
    for i in s:
        if i not in b:
            b.append(i)
    return b        
print(unique(a))

"""4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically. """
items=[n for n in input("enter words seprated by -: ").split('-')]
items.sort()
print('-'.join(items))

"""5. Write a program that accepts a sequence of lines as input and prints the lines 
after making all characters in the sentence capitalized. 
"""
lines = []
while True:
    l = input("Enter lines here: ")
    if l:
        lines.append(l.upper())
    else:
        break
    
    print(lines)

"""6. Define a function that can receive two integral numbers in string form and compute their sum and print it in console. """
def sumStrings (a,b):
	sum = int(a) + int(b)
	return sum 
s = sumStrings('9','10')
print(s)

"""7.        Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line. """
s1 = input("String 1: ")
s2 = input("String2: ")

def longerString(s1,s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    elif len(s1) == len(s2):
        print(s1)
        print(s2)
    else:
        pass    


longerString(s1,s2)

"""8.        Define a function which can generate and print a 
tuple where the value are square of numbers between 1 and 20"""
def printSquare():
    l = []
    for i in range(1,21):
        l.append(i**2)
    tup = tuple(l)
    print(tup)
    print(type(tup))
printSquare()    

"""9.Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.  

Example: If the limit is 3 , it should print: 

0 EVEN 

1 ODD 

2 EVEN 

3 ODD 
"""

def oddEven(limit):
    for i in range(1,limit+1):
        if i%2 != 0:
            print(i, ' Odd')
        elif i%2 == 0:
            print(i, ' Even')

oddEven(10)        
 
    
"""10. Write a program which can filter() to make a list
 whose elements are even number between 1 and 20 ( both included)
"""
def even():
    even_n = []
    for i in range(1,21): #modify range here
        if i %2 == 0:
            even_n.append(i)
    print(even_n) 

even()           

"""11. Write a program which can map() and filter() to make a list 
whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10] 

Hints: Use map() to generate a list. 

          Use filter() to filter elements of a list 

            Use lambda to define anonymous functions """

nums = [1,2,3,4,5,6,7,8,9,10]
eve_sq = list(map(lambda x: x**2, filter(lambda x: x%2 == 0, nums)))
print(eve_sq)

"""
12. Write a function to compute 5/0 and use try/except to catch the exceptions 
"""
try:
    x = 5/0
except: 
    print("Can not divide by 0")    

"""13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce 

Goal : Turn [1,2,3,4,5,6,7] to 1234567  """
from functools import reduce
import operator
l13= [[1,2,3],[4,5],[6,7,8]]
lred= reduce(operator.add, l13)
print(lred)

"""
(i) def foo(): 

    try: 

        return 1 

    finally: 

        return 2 

k = foo() 

print(k) 

 
(ii) def a(): 

    try: 

        f(x, 4) 

    finally: 

        print('after f') 

    print('after f?') 

a() 
"""
def foo(): 

    try: 

        return 1 

    finally: 

        return 2 

k = foo() 

print(k) 
#####################
def a(): 

    try: 

        f(x, 4) 

    finally: 

        print('after f') 

    print('after f?') 
