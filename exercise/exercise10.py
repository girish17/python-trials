import random
rn = random.choice(range(1000, 10000))
rnlist = list(str(rn))
choice = 'no'
cows = 0
bulls = 0
while choice == 'no':
    n = input('[write 0000 to give up.] enter a 4-digit number: ')
    a = n[0::5]
    b = n[1::4]
    c = n[2::4]
    d = n[3::4]
    ra = int(rnlist[0])
    rb = int(rnlist[1])
    rc = int(rnlist[2])
    rd = int(rnlist[3])
    if int(n) == rn:
        print('You Won!')
        choice = 'yes'
    else:
        if int(a) == ra:
            cows += 1
        else:
            if a in rnlist:
                bulls += 1
        if int(b) == rb:
            cows += 1
        else:
            if b in rnlist:
                bulls += 1
        if int(c) == rc:
            cows += 1
        else:
            if c in rnlist:
                bulls += 1    
        if int(d) == rd:
            cows += 1
        else:
            if d in rnlist:
                bulls += 1
        print('cows: ', cows)
        cows = 0
        if cows != 4:
            print('bulls: ', bulls)
        bulls = 0
        if n == '0000':
            print(rn, 'was the number!')
            break
