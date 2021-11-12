import random
import math

from src.consts.metro_consts import (
    DEFAULT_MAP_WIDTH,
    DEFAULT_MAP_HEIGHT,
    DEFAULT_NUM_STATIONS,
    DEFAULT_NUM_LINES,
    TOP_LEFT_CORNER,
    TOP_RIGHT_CORNER,
    BOTTOM_LEFT_CORNER,
    BOTTOM_RIGHT_CORNER,
    VERTICAL_PIPE,
    HORIZONTAL_PIPE,
)

def generate_stations(map_width, map_height, num_stations):
    stations = []
    for _ in range(num_stations):
        station = generate_random_location(map_width, map_height)
        stations.append(station)
    return stations


def generate_lines(map_width, map_height, stations, num_lines):
    lines = []
    for _ in range(num_lines):
        line = []
        middle_location = generate_random_location(map_width, map_height)
        vector = generate_vector()
        print_vector(vector)
        # while current_location['x'] not in (0, map_width) and current_location['y'] not in (0, map_height):
        current_location = middle_location
        while True:
            closest_station = get_closest_station(current_location, stations, line, map_width, map_height, vector, False)
            if closest_station == -1:
                break
            line.append(closest_station)
            current_location = stations[closest_station]
        current_location = middle_location
        line.insert(0, "X")
        while True:
            closest_station = get_closest_station(current_location, stations, line, map_width, map_height, vector, True)
            if closest_station == -1:
                break
            line.insert(0, closest_station)
            current_location = stations[closest_station]
        lines.append({"start": middle_location, "line": line})
    return lines


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
    print("######## Closest Station #########")
    print(f"vector: {vector}, is_inverse: {is_inverse}, current_location: {current_location}, desired_location: {desired_location}")
    print("##################################")
    for station in stations:
        if station_num not in line:
            cur_dist = calculate_distance(current_location, station)
            desired_dist = calculate_distance(desired_location, station)
            dist_discrepancy = cur_dist - desired_dist
            print(f"{station_num} - station: {station}, cur_dist: {cur_dist}, desired_dist: {desired_dist}, dist_discrepancy: {dist_discrepancy}")
            if dist_discrepancy > 0 and desired_dist < min_dist:
                selected_station = station_num
                min_dist = desired_dist
        station_num += 1
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"selected_station: {selected_station}")
    print()
    return selected_station


def calculate_distance(loc_1, loc_2):
    x_dist = loc_1['x'] - loc_2['x']
    y_dist = loc_1['y'] - loc_2['y']
    return math.sqrt(x_dist**2 + y_dist**2)

def print_vector(vector):
    horizontal_lines = "".join([HORIZONTAL_PIPE for _ in range(5)])
    if vector["x_vec"] < 0 and vector["y_vec"] < 0:
        print(f"{TOP_LEFT_CORNER}{horizontal_lines}{TOP_RIGHT_CORNER}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}{horizontal_lines}{VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE} x{VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}x {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{BOTTOM_LEFT_CORNER}{horizontal_lines}{BOTTOM_RIGHT_CORNER}")
    if vector["x_vec"] > 0 and vector["y_vec"] < 0:
        print(f"{TOP_LEFT_CORNER}{horizontal_lines}{TOP_RIGHT_CORNER}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}{horizontal_lines}{VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}x {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE} x{VERTICAL_PIPE}")
        print(f"{BOTTOM_LEFT_CORNER}{horizontal_lines}{BOTTOM_RIGHT_CORNER}")
    if vector["x_vec"] > 0 and vector["y_vec"] > 0:
        print(f"{TOP_LEFT_CORNER}{horizontal_lines}{TOP_RIGHT_CORNER}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE} x{VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}x {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}{horizontal_lines}{VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{BOTTOM_LEFT_CORNER}{horizontal_lines}{BOTTOM_RIGHT_CORNER}")
    if vector["x_vec"] < 0 and vector["y_vec"] > 0:
        print(f"{TOP_LEFT_CORNER}{horizontal_lines}{TOP_RIGHT_CORNER}")
        print(f"{VERTICAL_PIPE}x {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE} x{VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}{horizontal_lines}{VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{VERTICAL_PIPE}  {VERTICAL_PIPE}  {VERTICAL_PIPE}")
        print(f"{BOTTOM_LEFT_CORNER}{horizontal_lines}{BOTTOM_RIGHT_CORNER}")