choice = 'y'
shapes = {'1':'line', '2': 'angle', '3': 'triangle', '4': ['square', 'rectangle', 'rhombus', 'trapezoid', 'trapezium', 'quadrilateral', 'parallelogram'],
          '5': 'pentagon', '6': 'hexagon', '7': ['septagon', 'heptagon'], '8': 'octagon', '9': 'nonagon', '10': 'decagon',
          '11': ['hendecagon', 'undecagon', 'endecagon'], '12': 'dodecagon'}
while choice in ['y', 'Y', 'yes', 'Yes']:
    n = input("enter the number of sides. I'll tell you which shape has that many sides. Enter here: ")
    if n in shapes.keys():
        print(shapes[n])
    else:
        print("I don't know a shape with that many number of sides.")    
    choice = input("do you want to continue? (y/n): ")

