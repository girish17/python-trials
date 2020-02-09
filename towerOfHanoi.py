n = input("Enter number of discs: ")
def towerOfHanoi(num_of_discs, A, C, B):
    if num_of_discs==1:
        print "Move disc 1 from ", A, "to ", C
    else:
        towerOfHanoi(num_of_discs-1, A, B, C)
        print "Move disc", num_of_discs, "from ", A, "to ", C
        towerOfHanoi(num_of_discs-1, B, C, A)

towerOfHanoi(n, "A", "C", "B")
