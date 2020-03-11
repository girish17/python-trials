z = input("enter a symbol: ")
m = input("enter a number: ")
pattern = ''

for i in range(0, m):
    for j in range(0, m):
        pattern = pattern + ' ' + z
    pattern = pattern + '\n'
print pattern
