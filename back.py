import random
points = []
pointsValue = []
date = []
n = 6
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


def add_points(tud):
    for i in range(n):
        points[i][0] = '00' + str(i+1)
        points[i][1][0] = tud[0][i]
        points[i][1][1] = tud[1][i]


def add_points_value():
    for i in range(n):
        pointsValue[i][0] = '00' + str(i+1)
        for j in range(30):
            pointsValue[i][1][j][0] = j
            for h in range(3):
                pointsValue[i][1][j][1][0] = random.randint(60, 80)
                pointsValue[i][1][j][1][1] = random.randint(22, 27)
                pointsValue[i][1][j][1][2] = round(random.random(), 2) + random.randint(0, 10)


def get_measurements_by_id(ID):
    t = 0
    for i in range(n):
        if ID == pointsValue[i][0]:
            t = i
            break

    return pointsValue[t][1], ID


def get_mid_value():
    mid = []
    date0 = []
    for i in range(30):
        mid.append([])
        for j in range(3):
            mid[i].append(0)
    for i in range(n):
        for j in range(30):
            date0.append(j)
            for h in range(3):
                mid[j][h] += pointsValue[i][1][j][1][h]
    for i in range(30):
        for j in range(3):
            if j != 2:
                mid[i][j] = round(mid[i][j]/n)
            else:
                mid[i][j] = round(mid[i][j]/n, 2)
    return mid, date0


def get_points():
    return points, n


def get_date():
    return date


def get_tud():
    longitudes = [38.487501, 38.487501, 38.482901, 38.477501, 38.482901, 38.487501]
    latitudes = [54.786754, 54.790001, 54.790501, 54.793905, 54.793905, 54.793905]
    return longitudes, latitudes


add_date()
add_points(get_tud())
add_points_value()
get_mid_value()


