n = input("enter a positive number till which taxi cab numbers need to be generated:")

i = 1
a = 1
b = 1
p = 1
q = 1
while i != n:
    '''find out whether 'i' is a taxi cab number and print it'''
    while a != n:
        if a != b:
            while b != n:
                if b != p:
                    while p != n:
                        if p != q:
                            while q != n:
                                if q != a:
                                    if (a**3 + b**3) == (p**3 + q**3):
                                        print("Taxi cab number is: ", i)
                                q = q+1
                        p = p+1
                b = b+1
        a = a+1
    i = i+1
