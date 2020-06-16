'''
    Ask the user for a number and determine whether the number is prime or not.
'''
import math
n = int(input('enter a number: '))
prime = True
if n%2 == 0 and n != 2:
    print('composite because it is even and not two')
    prime = False
if n%2 != 0:
    sq = int(math.sqrt(n))
    for factor in range(3, sq):
        if n%factor == 0:
            
            print('composite, because', factor, 'is a factor of', n)
            prime = False
            break
       
if prime == True:
    print('prime')
    
    
    
