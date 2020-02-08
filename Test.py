add = []

a = 1
b = 5
ID = 5

add = [(a, [2, 3, 4]), (7, [6, 7, 8]), (5, [6, 7, 8]), (4, [6, 7, 8]), (1, [6, 7, 8])]
a = [1, 2, 3, 4, 5]


def specific_value(ID):
    t = 0
    for i in range(7):
        if ID == add[i][0]:
            t = i
            break
    print(i)

