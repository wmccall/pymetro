from logging import root
import random
import math

from pymetro.utils.debug_utils import (
    print_vector,
    print_current_info,
    print_station_details,
    print_selected_station,
)

def generate_stations(map_width, map_height, num_stations):
    stations = []
    for _ in range(num_stations):
        station = generate_random_location(map_width, map_height)
        stations.append(station)
    return stations


def generate_lines(map_width, map_height, stations, num_lines):
    lines = []
    touched_stations = []
    for _ in range(num_lines):
        root_station_num = int(random.random() * len(stations))
        root_station = stations[root_station_num]
        max_allowed_dist_from_line = math.sqrt(map_width**2 + map_height**2)/30
        vector = generate_vector()
        fitting_stations = find_fitting_stations(stations, root_station, max_allowed_dist_from_line, vector)
        lines.append({"start": root_station, "line": fitting_stations[0], "slope": vector['y_vec']/vector['x_vec'], "y_intercept": calculate_y_intercept(root_station, vector)})
        # lines.append({"start": root_station, "line": fitting_stations[1]})
    return {'lines': lines, 'touched_stations': touched_stations}


def generate_vector():
    return {"x_vec": (random.random()*2)-1, "y_vec": (random.random()*2)-1}


def find_fitting_stations(stations, root_station, max_allowed_dist_from_line, vector):
    y_intercept = calculate_y_intercept(root_station, vector)
    vector_degree = math.atan(vector['y_vec']/vector['x_vec'])
    fitting_stations = []
    for station in stations:
        dist_from_line = calculate_dist_from_line(station, vector, y_intercept)
        # print(dist_from_line)
        if dist_from_line <= max_allowed_dist_from_line:
            fitting_stations.append(station)
    print(f'fit: {fitting_stations}\n############################################')
    sorted_stations = sorted(fitting_stations, key=lambda station: station['x']*math.cos(vector_degree) - station['y']*math.sin(vector_degree))
    print(f'sort: {sorted_stations}\n++++++++++++++++++++++++++++++++++++++++++++')
    fitting_stations = sorted(fitting_stations, key=lambda station: station['x'])
    return [sorted_stations, fitting_stations]

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
    # print(f'a: {a}, b: {b}, c: {c}, x: {x}, y: {y}')
    return round(abs(a * x + b * y + c) / math.sqrt(a**2 + b**2), 5)


def generate_random_location(map_width, map_height):
    x = random.randint(1, map_width-1)
    y = random.randint(1, map_height-1)
    return {"x":x, "y":y}
