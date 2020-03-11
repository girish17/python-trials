import math

n = input("how many lines should the Pascal triangle have?")
pattern = ''
odd = 1

if n < 1:
    print"enter a bigger number"
elif n > 150:
    print"enter a smaller number"
else:

    while n > 0:
        spaces = n - 1
        '''print spaces'''
        while spaces > 0:
            pattern = pattern + ' '
            spaces = spaces - 1
        '''print Pascal number''' 
        pn = 1
        while pn > 0:
            r = 0
            while r <= n:
                pattern = pattern + ' ' + str(math.factorial(n)/((math.factorial(n-r)*math.factorial(r))))
                r = r+1 
                pn = pn - 1
        pattern = pattern + '\n'
        pn = pn + 1
        odd = odd + 2
        n = n - 1

    print pattern
    



