n = input("Enter a positive integer:")
num = n
sum = 0
if n<=0:
        print "invalid input"
else:
    while n>0:
        sum = sum + n**3
        n = n-1
    print "sum of cubes from1 to", num,"is",sum        
