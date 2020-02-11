n=input("enter a number: ")

def factorial(n):
    '''base case'''
    if n<1:
        return 1
    else:
        return n*factorial(n-1) #recursion step

print(factorial(n))
