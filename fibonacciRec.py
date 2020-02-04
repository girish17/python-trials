n = input("enter a number")
def fib(n):
    num1 = 1
    num2 = 1
    fibonacci = 1
    while n>0:
        if n<=2:
            fibonacci = 1
        else:
            fibonacci = num2+num1
            print(fibonacci)
            num1 = num2
            num2 = fibonacci
        n = n-1

fib(n)
