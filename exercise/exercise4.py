'''
  Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
  (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
  For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
f = int(input("enter a number"))
print([n for n in range(1,f+1) if f%n == 0])

