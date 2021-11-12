import random
import math

from src.utils.debug_utils import (
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
    connection_bends = {}
    for _ in range(num_lines):
        line = []
        middle_location = generate_random_location(map_width, map_height)
        vector = generate_vector()
        # print_vector(vector)
        # while current_location['x'] not in (0, map_width) and current_location['y'] not in (0, map_height):
        current_location = middle_location
        while True:
            closest_station = get_closest_station(current_location, stations, line, map_width, map_height, vector, False)
            if closest_station == -1:
                break
            line.append(closest_station)

            if len(line) > 2:
                prev_station = line[len(line)-2]
                connection_str = f"{prev_station},{closest_station}"
                connection_str_2 = f"{closest_station},{prev_station}"
                if connection_str not in connection_bends.keys():
                    bends = True if random.random() > .7 else False
                    connection_bends[connection_str] = bends
                    connection_bends[connection_str_2] = bends
            current_location = stations[closest_station]
        current_location = middle_location
        # line.insert(0, "X")
        while True:
            closest_station = get_closest_station(current_location, stations, line, map_width, map_height, vector, True)
            if closest_station == -1:
                break
            line.insert(0, closest_station)
            if len(line) > 2:
                prev_station = line[1]
                connection_str = f"{prev_station},{closest_station}"
                connection_str_2 = f"{closest_station},{prev_station}"
                if connection_str not in connection_bends.keys():
                    bends = True if random.random() > .7 else False
                    connection_bends[connection_str] = bends
                    connection_bends[connection_str_2] = bends
            current_location = stations[closest_station]
        lines.append({"start": middle_location, "line": line})
    return {'lines': lines, 'connection_bends': connection_bends}


def generate_vector():
    return {"x_vec": (random.random()*2)-1, "y_vec": (random.random()*2)-1}


def generate_random_location(map_width, map_height):
    x = random.randint(1, map_width-1)
    y = random.randint(1, map_height-1)
    return {"x":x, "y":y}


def generate_desired_location(current_location, vector, is_inverse):
    x = current_location['x'] + vector['x_vec'] * (-1 if is_inverse else 1)
    y = current_location['y'] + vector['y_vec'] * (-1 if is_inverse else 1)
    return {"x":x, "y":y}


def get_closest_station(current_location, stations, line, map_width, map_height, vector, is_inverse):
    desired_location = generate_desired_location(current_location, vector, is_inverse)
    min_dist = math.sqrt(map_width**2 + map_height**2)
    selected_station = -1
    station_num = 0
    # print_current_info(vector, is_inverse, current_location, desired_location)
    for station in stations:
        if station_num not in line:
            cur_dist = calculate_distance(current_location, station)
            desired_dist = calculate_distance(desired_location, station)
            dist_discrepancy = cur_dist - desired_dist
            # print_station_details(station_num, station, cur_dist, desired_dist, dist_discrepancy)
            if dist_discrepancy > 0 and desired_dist < min_dist:
                selected_station = station_num
                min_dist = desired_dist
        station_num += 1
    # print_selected_station(selected_station)
    return selected_station


def calculate_distance(loc_1, loc_2):
    x_dist = loc_1['x'] - loc_2['x']
    y_dist = loc_1['y'] - loc_2['y']
    return math.sqrt(x_dist**2 + y_dist**2)

# def get_destinations(location, vector, map_width, map_height):
#     x = location['x']
#     y = location['y']
#     m = vector['y_vec'] / vector['x_vec']
#     b = y - (m * x)
#     y_intercept = b
#     x_intercept = (0 - b) / m
#     y_end_intercept = (m * map_width) + b
#     x_end_intercept = (map_height - b) / m