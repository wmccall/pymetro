from pymetro.consts.metro_consts import (
    TOP_LEFT_CORNER,
    TOP_RIGHT_CORNER,
    BOTTOM_LEFT_CORNER,
    BOTTOM_RIGHT_CORNER,
    VERTICAL_PIPE,
    HORIZONTAL_PIPE,
)

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
    
def ascii_map(pymetro):
    map = [[" " for col_num in range(pymetro.map_width)] for row_num in range(pymetro.map_height)]
    station_num = 0
    print(pymetro.stations)
    print(pymetro.tracks_info)
    for station in pymetro.stations:
        map[station['y']][station['x']] = f"{station_num}"
        station_num += 1

    map.reverse()

    horizontal_lines = HORIZONTAL_PIPE.join([HORIZONTAL_PIPE for _ in range(pymetro.map_width+1)])

    top_border = f"{TOP_LEFT_CORNER}{horizontal_lines}{TOP_RIGHT_CORNER}"
    print(top_border)
    for row in map:
        slice = f"{VERTICAL_PIPE} {' '.join(row)} {VERTICAL_PIPE}"
        print(slice)
    bottom_border = f"{BOTTOM_LEFT_CORNER}{horizontal_lines}{BOTTOM_RIGHT_CORNER}"
    print(bottom_border)

def print_current_info(vector, is_inverse, current_location, desired_location):
    print("######## Closest Station #########")
    print(f"vector: {vector}, is_inverse: {is_inverse}, current_location: {current_location}, desired_location: {desired_location}")
    print("##################################")

def print_station_details(station_num, station, cur_dist, desired_dist, dist_discrepancy):
    print(f"{station_num} - station: {station}, cur_dist: {cur_dist}, desired_dist: {desired_dist}, dist_discrepancy: {dist_discrepancy}")

def print_selected_station(selected_station):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(f"selected_station: {selected_station}")
    print()
