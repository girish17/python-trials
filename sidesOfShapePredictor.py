''' @author: prince '''

choice = 'y'
shapes = {'1':'line', '2': 'angle', '3': 'triangle', '4': ['square', 'rectangle', 'rhombus', 'trapezoid', 'trapezium', 'quadrilateral', 'parallelogram'],
          '5': 'pentagon', '6': 'hexagon', '7': ['septagon', 'heptagon'], '8': 'octagon', '9': 'nonagon', '10': 'decagon',
          '11': ['hendecagon', 'undecagon', 'endecagon'], '12': 'dodecagon'}
while choice in ['y', 'Y', 'yes', 'Yes']:
    n = input("enter a shape. I'll tell you how many sides it has. Enter here: ")
    n = n.lower()
    for side, shapeName in shapes.items():
        if n in shapeName:
            print(side)
            found = True
            break
        else:
            found = False

    if found == False:
        print("I don't know that shape, you smart person.")    
    
    choice = input("do you want to continue? (y/n): ")
