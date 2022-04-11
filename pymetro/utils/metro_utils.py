import random
import math


def generate_stations(map_width, map_height, num_stations):
    stations = []

    for _ in range(num_stations):
        station = generate_random_location(map_width, map_height)
        stations.append(station)

    return stations


def generate_lines(map_width, map_height, stations, num_lines, num_hubs):
    lines = []
    touched_stations = set()
    root_stations = []

    for _ in range(num_hubs):
        root_station_num = int(random.random() * len(stations))
        while stations[root_station_num] in root_stations:
            root_station_num = int(random.random() * len(stations))
        root_stations.append(stations[root_station_num])

    for _ in range(num_lines):
        root_station = root_stations[int(random.random() * len(root_stations))]
        max_allowed_dist_from_line = math.sqrt(map_width**2 + map_height**2)/30
        vector = generate_vector()

        fitting_stations = find_fitting_stations(stations, root_station, max_allowed_dist_from_line, vector)
        lines.append({"start": root_station, "line": fitting_stations})
        calculate_angle_from_3_stations(fitting_stations[0], fitting_stations[1], fitting_stations[3])

        touched_stations = (*touched_stations, *fitting_stations)

    return {'lines': lines, 'touched_stations': touched_stations}


def generate_vector():
    return {"x_vec": (random.random()*2)-1, "y_vec": (random.random()*2)-1}


def find_fitting_stations(stations, root_station, max_allowed_dist_from_line, vector):
    y_intercept = calculate_y_intercept(root_station, vector)

    vector_degree = math.atan(vector['y_vec']/vector['x_vec'])
    correction_degree = math.radians(-1 * math.degrees(vector_degree))

    fitting_stations = []

    for station in stations:
        dist_from_line = calculate_dist_from_line(station, vector, y_intercept)
        if dist_from_line <= max_allowed_dist_from_line:
            fitting_stations.append(station)

    sorted_stations = sorted(fitting_stations, key=lambda station: station['x']*math.cos(correction_degree) - station['y']*math.sin(correction_degree))
    return sorted_stations

def calculate_distance(loc_1, loc_2):
    x_dist = loc_1['x'] - loc_2['x']
    y_dist = loc_1['y'] - loc_2['y']
    return math.sqrt(x_dist**2 + y_dist**2)


def calculate_y_intercept(root_station, vector):
    return root_station['y'] - (vector['y_vec']/vector['x_vec'])*root_station['x']


def calculate_dist_from_line(station, vector, y_intercept):
    x = station['x']
    y = station['y']
    a = -1 * vector['y_vec']
    b = vector['x_vec']
    c = -1 * y_intercept * b
    return round(abs(a * x + b * y + c) / math.sqrt(a**2 + b**2), 5)


def calculate_angle_from_3_stations(s1, s2, s3):
    s1_s2_vector = (s1['y']-s2['y']),(s1['x']-s2['x'])
    s2_s3_vector = (s2['y']-s3['y']),(s2['x']-s3['x'])
    dot_prod = s1_s2_vector[0]*s2_s3_vector[0] + s1_s2_vector[1]*s2_s3_vector[1]
    s1_s2_dist = calculate_distance(s1, s2)
    s2_s3_dist = calculate_distance(s2, s3)
    return 180 - math.degrees(math.acos(dot_prod/(s1_s2_dist*s2_s3_dist)))


def generate_random_location(map_width, map_height):
    x = random.randint(1, map_width-1)
    y = random.randint(1, map_height-1)
    return {"x":x, "y":y}
