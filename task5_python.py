"""1. Write a program to Python find the values which is not divisible 3
 but is should be a multiple of 7. 
Make sure to use only higher order function. """
l1 = list(range(1,101))
# print(l1)
res1 = filter(lambda x: (x%3 != 0 and x%7 == 0), l1)
print(list(res1))

"""2. Write a program in Python to  multiple the element of list 
by itself using a traditional function and pass the function to map to complete the operation. 
"""
l2 = list(range(1,11))
def multiply(n):
    return n*n
   
res2 = map(multiply, l2)
print(list(res2))

"""3.Write a program to Python find out the character in 
a string which is uppercase using list comprehension. """
l3 = [letter for letter in 'This Is A TEST String' if letter.isupper()]
print(l3)

"""4. Write a program to construct a dictionary from the two lists containing the names of students 
and their corresponding subjects. The dictionary should maps the students 
with their respective subjects. Let’s see how to do this 
using for loops and dictionary comprehension. HINT-Use Zip function also """

student = ['Smit', 'Jaya', 'Rayyan'] 
subject = ['CSE', 'Networking', 'Operating System'] 

res4 = dict(zip(student, subject))
print(res4)

"""6. Write a program in Python using generators to reverse the string. 
Input String = “Consultadd Training” """
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("Consultadd Training"):
    print(char)

"""7. Write any example on decorators. """
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(10,2)    

