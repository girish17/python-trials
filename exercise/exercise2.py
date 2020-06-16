'''
    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
'''
# @author: prince
n = input("Enter a number. I will tell you if it's odd or even: ")
n = int(n)
a = n%2
if a == 1:
    print(n, "is an odd number")
else:
    print(n, "is an even number")
