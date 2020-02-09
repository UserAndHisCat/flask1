import random
points = []
measurements = []


points = [
    {"id": 1, "latitude": 54.818231, "longitude": 38.549497, "comment": "Первый!!"},
    {"id": 2, "latitude": 54.800000, "longitude": 38.570000},
    {"id": 3, "latitude": 54.740000, "longitude": 38.600000},
    {"id": 4, "latitude": 54.770000, "longitude": 38.650000},
    {"id": 5, "latitude": 54.787667, "longitude": 38.697472, "comment": "The last one"}
]

measurements = [
    {"point_id": 1, "timestamp": 1, "temperature": 20, "humidity": 17, "acidity": 5.5},
    {"point_id": 1, "timestamp": 2, "temperature": 21, "humidity": 16, "acidity": 5.5},
    {"point_id": 1, "timestamp": 3, "temperature": 22, "humidity": 15, "acidity": 5.5},
    {"point_id": 1, "timestamp": 4, "temperature": 23, "humidity": 14, "acidity": 5.5},
    {"point_id": 1, "timestamp": 5, "temperature": 24, "humidity": 13, "acidity": 5.5},

    {"point_id": 2, "timestamp": 1, "temperature": 20, "humidity": 17, "acidity": 5.5},
    {"point_id": 2, "timestamp": 2, "temperature": 21, "humidity": 17, "acidity": 5.4},
    {"point_id": 2, "timestamp": 3, "temperature": 22, "humidity": 17, "acidity": 5.3},
    {"point_id": 2, "timestamp": 4, "temperature": 23, "humidity": 17, "acidity": 5.2},
    {"point_id": 2, "timestamp": 5, "temperature": 24, "humidity": 17, "acidity": 5.1},

    {"point_id": 3, "timestamp": 1, "temperature": 20, "humidity": 17, "acidity": 5.5},
    {"point_id": 3, "timestamp": 2, "temperature": 20, "humidity": 18, "acidity": 5.4},
    {"point_id": 3, "timestamp": 3, "temperature": 20, "humidity": 19, "acidity": 5.3},
    {"point_id": 3, "timestamp": 4, "temperature": 20, "humidity": 20, "acidity": 5.2},
    {"point_id": 3, "timestamp": 5, "temperature": 20, "humidity": 21, "acidity": 5.1},

    {"point_id": 4, "timestamp": 1, "temperature": 20, "humidity": 17, "acidity": 5.5},
    {"point_id": 4, "timestamp": 2, "temperature": 21, "humidity": 16, "acidity": 5.4},
    {"point_id": 4, "timestamp": 3, "temperature": 22, "humidity": 15, "acidity": 5.3},
    {"point_id": 4, "timestamp": 4, "temperature": 23, "humidity": 14, "acidity": 5.2},
    {"point_id": 4, "timestamp": 5, "temperature": 24, "humidity": 13, "acidity": 5.1},

    {"point_id": 5, "timestamp": 1, "temperature": 20, "humidity": 17, "acidity": 5.5},
    {"point_id": 5, "timestamp": 2, "temperature": 19, "humidity": 16, "acidity": 5.6},
    {"point_id": 5, "timestamp": 3, "temperature": 18, "humidity": 15, "acidity": 5.7},
    {"point_id": 5, "timestamp": 4, "temperature": 17, "humidity": 14, "acidity": 5.6},
    {"point_id": 5, "timestamp": 5, "temperature": 16, "humidity": 13, "acidity": 5.5},
]


def get_points_all():
    return points


def get_measurements_all():
    return measurements


def get_measurements_by_id(id):
    result = []
    id = int(id)
    for measurement in measurements:
        if id == measurement['point_id']:
            result.append(measurement)

    return result

