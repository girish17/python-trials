import math

n = input("Please enter n: ")
r = input("Please enter r: ")
if n >= r:
    print math.factorial(n) / ( math.factorial(n-r) * math.factorial(r) )
else:
    print "n should be greater than or equal to r"
