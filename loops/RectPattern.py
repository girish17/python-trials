z = input("enter a symbol: ")
m = input("enter the width: ")
l = input("enter the height: ")
pattern = ''

for i in range(0, l):
    for j in range(0, m):
        pattern = pattern + ' ' + z
    pattern = pattern + '\n'
print pattern
