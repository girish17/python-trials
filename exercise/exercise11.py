import math
#@author prince
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input("enter a number, and we'll see if it's in the list: "))
low = 0
high = 9
listLength = len(x)
def binarysearch(n, x, low, high):
    mid = math.ceil((low + high)/2)
    if mid >= 0 and mid < listLength:  
        if n == x[mid]:
            return True
        if n < x[mid]:
            high = mid -1

        if n > x[mid]:
            low = mid + 1

        return binarysearch(n, x, low, high)
    else:
        return False
print(binarysearch(n, x, low, high))
