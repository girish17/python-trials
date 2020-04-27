n=input("Enter a number till which the sequence has to be generated: ")
def seq(n):
    '''base case'''
    if n<=2:
        return 1
    else:
        return seq(n-2)+seq(n-1)
i=1
while i<=n:
    print(seq(i))
    i=i+1
