n = input("Enter a positive integer: ")
num = n
sum = 0
if n<=0:
    print "Invalid input"
else:
    while n>0:
        sum = sum + n**2
        n = n-1
    print "sum of squares from 1 to", num, "is ", sum
