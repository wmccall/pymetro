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
