choice = "y"
while choice in ("y", "yes", "Yes"):
    sum = 0
    number = input("Enter a number: ")
    if number<1:
        print "not a whole and positive number"
    else:
        sum = number*(2*number+1)*(number+1)/6
        print sum
    choice = input("Would you like to run this program again ('y' or 'n')? ")
