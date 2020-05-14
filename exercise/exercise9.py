import random
num = 0
while num < 5:
    password = random.choice(["Throwing", "Catching", "Active", "Eating", "Coding", "Sitting", "Watching", "Destroying", "Boarding", "Gaming", "Folding", "Running"])+random.choice(["Chair", "Teammate", "Brownie", "Closet", "Box", "Blanket", "Carpet", "Pillow", "Muffin", "Console", "Cookie", "Cake"])+str(random.choice(range(1, 10000)))
    print(password)
    num = num+1
    if num == 5:
        break
