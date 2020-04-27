# @author prince
import datetime

n = input('Enter your age. I will tell you when you would turn 100 years old: ')
n = int(n)
currentYear = int(datetime.datetime.now().year)
an = ((currentYear - n)+100)
if n < 0:
    print('invalid number')
elif n > currentYear:
    print("Congrats! you are a centurian! You turned 100 in", abs(an), "BC")
elif n > 100:
    print("Congrats! you are a centurian! You turned 100 in", an)
else:
    print("you will turn 100 in: ", an)
