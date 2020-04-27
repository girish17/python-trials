n = input("Enter a number: ")
num = n
factorial = 1
while n>0:
    factorial = factorial*n
    n = n-1 

print("Factorial of "+ str(num) +"  is: "+ str(factorial))
