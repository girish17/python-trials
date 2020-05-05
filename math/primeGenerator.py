import math
x = int(input('enter a number: '))
for num in range(2, x):
    factorCount = 2
    for factor in range(2, int(math.sqrt(num)+1)):
        if num%factor == 0:
            factorCount += 1
    if factorCount == 2:
        print(num)
        
