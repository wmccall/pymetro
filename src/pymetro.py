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
from src.utils.metro_utils import (
    generate_stations,
    generate_lines,
)

class PyMetro:
    def __init__(self,
                 map_width=DEFAULT_MAP_WIDTH,
                 map_height=DEFAULT_MAP_HEIGHT,
                 num_stations=DEFAULT_NUM_STATIONS,
                 num_lines=DEFAULT_NUM_LINES):
        self.map_width = map_width
        self.map_height = map_height
        self.num_stations = num_stations
        self.num_lines = num_lines
    
    def details(self):
        print(f"Map Width: {self.map_width}")
        print(f"Map Height: {self.map_height}")
        print(f"Number of Stations: {self.num_stations}")
        print(f"Number of Train Lines: {self.num_lines}")

    def generate(self):
        self.stations = generate_stations(self.map_width, self.map_height, self.num_stations)
        self.lines = generate_lines(self.map_width, self.map_height, self.stations, self.num_lines)

    def ascii_map(self):
        map = [[" " for col_num in range(self.map_width)] for row_num in range(self.map_height)]
        station_num = 0
        print(self.stations)
        print(self.lines)
        for station in self.stations:
            map[station['y']][station['x']] = f"{station_num}"
            station_num += 1
        for line in self.lines:
            l = line["start"]
            map[l['y']][l['x']] = "X"

        map.reverse()

        horizontal_lines = HORIZONTAL_PIPE.join([HORIZONTAL_PIPE for _ in range(self.map_width+1)])

        top_border = f"{TOP_LEFT_CORNER}{horizontal_lines}{TOP_RIGHT_CORNER}"
        print(top_border)
        for row in map:
            slice = f"{VERTICAL_PIPE} {' '.join(row)} {VERTICAL_PIPE}"
            print(slice)
        bottom_border = f"{BOTTOM_LEFT_CORNER}{horizontal_lines}{BOTTOM_RIGHT_CORNER}"
        print(bottom_border)