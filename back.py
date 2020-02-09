import random
points = []
pointsValue = []
date = []
n = random.randint(4, 7)
a = ''

for i in range(n):
    points.append([a, []])
    for j in range(2):
        points[i][1].append([])

for i in range(n):
    pointsValue.append([a, []])
    for j in range(30):
        pointsValue[i][1].append([a, []])
        for h in range(3):
            pointsValue[i][1][j][1].append([])


def add_date():
    year_number = 1
    month_number = 6
    week_number = 5
    for y in range(year_number):
        for m in range(1, month_number + 1):
            for w in range(week_number):
                date.append(str(1 + w * 7) + ' . ' + str(m) + ' . ' + str(2019 + y))


def add_points():
    for i in range(n):
        points[i][0] = '00' + str(i+1)
        points[i][1][0] = str(random.randint(11, 100)) + '.' + str(random.randint(1000000, 10000000))
        points[i][1][1] = str(random.randint(11, 100)) + '.' + str(random.randint(1000000, 10000000))


def add_points_value():
    for i in range(n):
        pointsValue[i][0] = '00' + str(i+1)
        for j in range(30):
            pointsValue[i][1][j][0] = j
            for h in range(3):
                pointsValue[i][1][j][1][0] = random.randint(60, 80)
                pointsValue[i][1][j][1][1] = random.randint(22, 27)
                pointsValue[i][1][j][1][2] = random.random() + random.randint(0, 10)


def get_measurements_by_id(ID):
    t = 0
    for i in range(n):
        if ID == pointsValue[i][0]:
            t = i
            break

    return pointsValue[t][1], ID


def get_points():
    return points, n


def get_date():
    return date


add_date()
add_points()
add_points_value()

