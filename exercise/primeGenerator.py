n = int(input("Number till which prime numbers need to be generated: "))
factorCount = 2
for primeNum in range(2, n):
    if primeNum%2 == 0 and primeNum != 2:
        factorCount += 1
    else:
        for factor in range(3, n, 2):
            if primeNum%factor == 0:
                factorCount += 1

    if factorCount == 2:
        print(primeNum)
                
