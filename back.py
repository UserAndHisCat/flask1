import random
points = []
pointsValue = []
longPoints = []
widthPoints = []
n = random.randint(4, 7)
a = ''

for i in range(n):
    points.append([a, []])
    for j in range(2):
        points[i][1].append([])

for i in range(n):
    pointsValue.append([a, []])
    for j in range(24):
        pointsValue[i][1].append([a, []])
        for h in range(3):
            pointsValue[i][1][j][1].append([])


def add_points():
    for i in range(n):
        points[i][0] = '00' + str(i+1)
        points[i][1][0] = str(random.randint(11, 100)) + '.' + str(random.randint(1000000, 10000000))
        points[i][1][1] = str(random.randint(11, 100)) + '.' + str(random.randint(1000000, 10000000))
    return points


def add_points_value():
    for i in range(n):
        pointsValue[i][0] = '00' + str(i+1)
        for j in range(24):
            pointsValue[i][1][j][0] = j
            for h in range(3):
                pointsValue[i][1][j][1][0] = random.randint(10, 100)
                pointsValue[i][1][j][1][1] = random.randint(10, 100)
                pointsValue[i][1][j][1][2] = random.randint(10, 100)
    return pointsValue


def specific_value(id):
    for i in range(n):
        if id == pointsValue[i][0]:
            print('fhfhf')


add_points()
add_points_value()