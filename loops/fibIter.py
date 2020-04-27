n = input('Enter a number till which the sequence has to printed: ')
i=1
currentNum=1
num1=1
num2=1
while i<=n:
    if i<=2:
        print(currentNum)
    else: 
        currentNum = num1+num2
        print(currentNum)
        num1 = num2
        num2 = currentNum

    i = i+1
