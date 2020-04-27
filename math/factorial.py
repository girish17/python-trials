n = input("Enter a number for which factorial has to be determined: ")

def fact(n):
    factorial = 1
    while n>0:
        factorial = factorial * n
        n = n-1

    return factorial

print(fact(n))
