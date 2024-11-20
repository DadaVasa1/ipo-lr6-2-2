import random
num =  [-15, -4, -2, -7, 0, 3, 5, 12, 7]
width = random.randint(4, 8) 
height = random.randint(4, 8) 


matrix = []

for i in range(height):
    height2 = []
    for i in range(width):
        height2.append(random.choice(num))
    matrix.append(height2)

for i in matrix:
    for el in i:
        print(el, " ", end="" )
    print()
