import random
num = 0
while num < 5:
    password = random.choice(["Throwing", "Catching", "Active", "Eating", "Coding", "Sitting", "Watching", "Destroying", "Boarding", "Gaming"])+random.choice(["Chair", "Teammate", "Brownie", "Closet", "Box", "Blanket", "Carpet", "Pillow", "Muffin", "Console"])+str(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(password)
    num = num+1
    if num == 5:
        break
